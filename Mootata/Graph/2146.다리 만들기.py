from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
number = 1
answer = float('inf')

def count_land(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    graph[x][y] = number
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:
                continue
            
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = number
                visited[nx][ny] = True

def bridge(x, y, num):
    q = deque()
    q.append((x, y, 0))
    
    while q:
        x, y, dist = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny] or graph[nx][ny] == num:
                continue
            
            if graph[nx][ny] != 0 and graph[nx][ny] != num:
                return dist
            
            q.append((nx, ny, dist + 1))
            visited[nx][ny] = True
    return float('inf')

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] != 0:
            count_land(i, j)
            number += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            visited = [[False for _ in range(n)] for _ in range(n)]
            answer = min(answer, bridge(i, j, graph[i][j]))

print(answer)