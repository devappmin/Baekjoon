import sys
from collections import deque

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

n, m, t = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

gram_point = ()

for y in range(n):
    for x in range(m):
        if graph[y][x] == 2:
            gram_point = (y, x)
            break

def without_gram():
    q = deque([(0, 0)])
    visited = [[0] * m for _ in range(n)]
    visited[n - 1][m - 1] = float('inf')

    while q:
        y, x = q.popleft()

        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]

            if not (0 <= ny < n and 0 <= nx < m):
                continue

            if visited[ny][nx] and visited[ny][nx] != float('inf'):
                continue

            if graph[ny][nx] == 1:
                continue

            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))

    return visited[n - 1][m - 1]

def with_gram():
    q = deque([(0, 0)])
    visited = [[0] * m for _ in range(n)]
    visited[n - 1][m - 1] = float('inf')

    while q:
        y, x = q.popleft()

        if (y, x) == gram_point:
            return visited[gram_point[0]][gram_point[1]] + \
                m + n - gram_point[0] - gram_point[1] - 2

        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]

            if not (0 <= ny < n and 0 <= nx < m):
                continue

            if visited[ny][nx] and visited[ny][nx] != float('inf'):
                continue

            if graph[ny][nx] == 1:
                continue

            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))

    return visited[n - 1][m - 1]


minimum_time = min(with_gram(), without_gram())
print(minimum_time if minimum_time <= t else "Fail")
