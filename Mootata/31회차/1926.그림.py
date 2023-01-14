from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
answer = []

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    size = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny] or paper[nx][ny] == 0:
                continue
            
            q.append((nx, ny))
            visited[nx][ny] = True
            size += 1
            
    return size

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and not visited[i][j]:
            answer.append(bfs(i, j))

if answer:
    print(len(answer), max(answer), sep = '\n')
else:
    print(0, 0, sep = '\n')