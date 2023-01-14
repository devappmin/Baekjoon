n, m = map(int, input().split())
answer = []

def recursive(start):
    if start == m:
        print(*answer)
        return
    
    for i in range(1, n + 1):
        answer.append(i)
        recursive(start + 1)
        answer.pop()

recursive(0)