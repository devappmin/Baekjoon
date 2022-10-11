import sys
from collections import defaultdict
from heapq import heappush, heappop


def solution():
    n, d, c = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)

    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append((a, s))
    
    dists = {node: float('inf') for node in range(1, n + 1)}
    dists[c] = 0

    q = [(0, c)]

    while q:
        cur_dist, cur_node = heappop(q)

        if dists[cur_node] < cur_dist:
            continue

        for new_node, new_dist in graph[cur_node]:
            d = new_dist + cur_dist

            if d < dists[new_node]:
                dists[new_node] = d
                heappush(q, (dists[new_node], new_node))
    print(len([x for x, y in dists.items() if y != float('inf')]), max([x for x in dists.values() if x != float('inf')]))


for _ in range(int(sys.stdin.readline())):
    solution()