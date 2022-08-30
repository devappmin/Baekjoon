import sys

n = int(input())
board = [list(input()) for _ in range(n)]
answer = 0

dx, dy = [1, 0], [0, 1] # 하, 우

def check():
    row_cnt, col_cnt = 1, 1
    row_max, col_max = 0, 0
    for i in range(n):
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1]:
                row_cnt += 1
            else:
                row_cnt = 1
            row_max = max(row_max, row_cnt)
            
            if board[j][i] == board[j + 1][i]:
                col_cnt += 1
            else:
                col_cnt = 1
            col_max = max(col_max, col_cnt)
            
        row_cnt = 1
        col_cnt = 1
    return max(row_max, col_max)

for x in range(n):
    for y in range(n):
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if board[x][y] != board[nx][ny]:
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                answer = max(answer, check())
                board[nx][ny], board[x][y] = board[x][y], board[nx][ny]

print(answer)