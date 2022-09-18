import sys
from collections import deque, defaultdict

n = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = defaultdict(list)
visited = [0] * (n + 1)

for _ in range(m):
    fr, to = map(int, sys.stdin.readline().split())
    graph[fr].append(to)
    graph[to].append(fr)


visited[start] = 1
q = deque([start])

while q:
    s = q.popleft()

    if visited[end]:
        break

    for node in graph[s]:
        if visited[node]:
            continue

        visited[node] = visited[s] + 1
        q.append(node)

print(-1 if not visited[end] else visited[end] - 1)
