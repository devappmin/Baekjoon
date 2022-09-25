from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
hx, hy = [-2, -2, -1, 1, 2, 2, 1, -1], [-1, 1, 2, 2, 1, -1, -2, -2]

k = int(input())
w, h = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(h)]
visited = [[[0 for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]
# x, y, h 인 경우 x, y 의 좌표로 h번의 말의 이동으로 이동했을 때 해당 위치까지 도달하는 동작 수

def bfs():
    q = deque([[0, 0, k]])
    
    while q:
        x, y, jump = q.popleft()
        
        if x == h - 1 and y == w - 1:
            return visited[x][y][jump]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= h or ny >= w or visited[nx][ny][jump] or board[nx][ny] == 1:
                continue
            
            visited[nx][ny][jump] = visited[x][y][jump] + 1
            q.append((nx, ny, jump))
            
        if jump > 0:
            for i in range(8):
                hnx, hny = x + hx[i], y + hy[i]
                
                if hnx < 0 or hny < 0 or hnx >= h or hny >= w or visited[hnx][hny][jump - 1] or board[hnx][hny] == 1:
                    continue
                
                visited[hnx][hny][jump - 1] = visited[x][y][jump] + 1
                q.append((hnx, hny, jump - 1))
    return -1
print(bfs())