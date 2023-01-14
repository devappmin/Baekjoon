from heapq import heappop, heappush

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n = int(input())
maze = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
def bfs():
    q = []
    heappush(q, (0, 0, 0))
    visited[0][0] = True
    
    while q:
        black, x, y = heappop(q)
        
        if x == n - 1 and y == n - 1:
            return black
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:
                continue
            
            visited[nx][ny] = True
            if maze[nx][ny] == 0:
                heappush(q, (black + 1, nx, ny))
            else:
                heappush(q, (black, nx, ny))

print(bfs())