from collections import deque

dx, dy = [-1, 1 , 0, 0], [0, 0, -1, 1]

n, m, k = map(int, input().split())
graph = [['.' for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
result = []

for i in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = '#'

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    size = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny] or graph[nx][ny] == '.':
                continue
            
            q.append((nx, ny))
            visited[nx][ny] = True
            size += 1
    
    return size

for x in range(n):
    for y in range(m):
        if graph[x][y] == '#' and not visited[x][y]:
            result.append(bfs(x, y))

print(max(result))