from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

k = int(input())
w, h = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(h)]

def bfs():
    q = deque((0, 0, 1))
    visited[0][0] = True
    
    while q:
        x, y, jump = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= h or ny >= w or visited[nx][ny]:
                continue
            
            