import sys
from collections import deque

hy, hx = [2, 2, 1, 1, -1, -1, -2, -2], [1, -1, 2, -2, 2, -2, 1, -1]
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
visited = [[[False] * (k + 1) for _ in range(w)] for _ in range(h)]
visited[0][0][k] = True

q = deque([(0, 0, k, 0)])

answer = -1

while q:
    y, x, ck, count = q.popleft()

    if y == ( h - 1 ) and x == ( w - 1 ):
        answer = count
        break

    if ck > 0:
        for idx in range(8):
            ny, nx = y + hy[idx], x + hx[idx]

            if not (0 <= ny < h and 0 <= nx < w):
                continue

            if graph[ny][nx]:
                continue

            if visited[ny][nx][ck - 1]:
                continue

            visited[ny][nx][ck - 1] = True
            q.append((ny, nx, ck - 1, count + 1))
    
    for idx in range(4):
        ny, nx = y + dy[idx], x + dx[idx]

        if not (0 <= ny < h and 0 <= nx < w):
            continue

        if graph[ny][nx]:
            continue

        if visited[ny][nx][ck]:
            continue

        visited[ny][nx][ck] = True
        q.append((ny, nx, ck, count + 1))

print(answer)