n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def stair(stairs):
    for i in range(n - 1):
        if abs(stairs[i] - stairs[i + 1]) > 1:
            return False
        elif stairs[i] > stairs[i + 1]:
            # 이전 높이가 더 높을 때, 오른쪽 확인
            for j in range(l):
                if i + 1 + j >= n or stairs[i + 1] != stairs[i + 1 + j] or slope[i + 1 + j]:
                    return False
                elif stairs[i + 1] == stairs[i + 1 + j]:
                    slope[i + 1 + j] = True     
        elif stairs[i] < stairs[i + 1]:
            # 다음 높이가 더 높을 때, 왼쪽 확인
            for j in range(l):
                if i - j < 0 or stairs[i] != stairs[i - j] or slope[i - j]:
                    return False
                elif stairs[i] == stairs[i - j]:
                    slope[i - j] = True   
    return True

for i in range(n):
    slope = [False for _ in range(n)]
    
    if stair(list(graph[i][j] for j in range(n))):
        answer += 1

for j in range(n):
    slope = [False for _ in range(n)]
    
    if stair(list(graph[i][j] for i in range(n))):
        answer += 1

print(answer)