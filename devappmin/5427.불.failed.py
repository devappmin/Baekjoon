import sys
from collections import deque

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

def solution():
    w, h = map(int, sys.stdin.readline().split())

    graph = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
    fires = deque()
    temp_fires = deque()
    user = deque()
    temp_user = deque()
    visited = [[0] * w for _ in range(h)]

    for y in range(h):
        for x in range(w):
            if graph[y][x] == '*':
                fires.append((y, x))
                continue

            if graph[y][x] == '@':
                temp_user.append((y, x))
                visited[y][x] = 1
    
        
    while temp_user or user:
        if not user:
            user = temp_user
            temp_user = deque()

            for fy, fx in fires:
                for idx in range(4):
                    nfy, nfx = fy + dy[idx], fx + dx[idx]

                    if not (0 <= nfy < h and 0 <= nfx < w):
                        continue

                    if graph[nfy][nfx] == '#':
                        continue

                    if graph[nfy][nfx] == '*':
                        continue

                    graph[nfy][nfx] = '*'
                    temp_fires.append((nfy, nfx))
            
            fires = temp_fires
            temp_fires = deque()

        y, x = user.popleft()

        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]

            if not (0 <= ny < h and 0 <= nx < w):
                print(visited[y][x])
                return
            
            if graph[ny][nx] == '#':
                continue

            if graph[ny][nx] == '*':
                continue
            
            if visited[ny][nx]:
                continue

            visited[ny][nx] = visited[y][x] + 1
            temp_user.append((ny, nx))

    print("IMPOSSIBLE")

for _ in range(int(sys.stdin.readline())):
    solution()