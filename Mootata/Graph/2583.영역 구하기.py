from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

m, n, k = map(int, input().split())
paper = [[0 for _ in range(m)] for _ in range(n)]
answer = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[i][j] = 1

def bfs(x, y):
    q = deque()
    q.append((x, y))
    paper[x][y] = 1
    count = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m or paper[nx][ny] == 1:
                continue
            
            paper[nx][ny] = 1
            q.append((nx, ny))
            count += 1
    return count



for i in range(n):
    for j in range(m):
        if paper[i][j] == 0:
            answer.append(bfs(i, j))

print(len(answer))
print(*sorted(answer))