import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, sys.stdin.readline().split())
visited = [0] * (n + 1)

graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

weight = 0

def dfs(cur):
    global weight

    visited[cur] = weight + 1

    for node in sorted(graph[cur]):
        if not visited[node]:
            weight += 1
            dfs(node)

dfs(r)

print(*visited[1:], sep='\n')