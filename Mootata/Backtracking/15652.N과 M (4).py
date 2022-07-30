n, m = map(int, input().split())
answer = []

def recursive(start):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(start, n + 1):
        answer.append(i)
        recursive(i)
        answer.pop()

recursive(1)