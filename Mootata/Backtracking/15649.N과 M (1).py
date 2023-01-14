n, m = map(int, input().split())
answer = []
visited = [False for _ in range(n + 1)]

def recursive(start):
    if start == m:
        print(*answer)
        return
    
    for i in range(1, n + 1):
        if not visited[i]:
            answer.append(i)
            visited[i] = True
            recursive(start + 1)
            answer.pop()
            visited[i] = False

recursive(0)