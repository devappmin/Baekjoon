def recursive(start):
    if len(answer) == 6:
        print(*answer)
        return
    
    for i in nums:
        if not visited[i] and start < i:
            answer.append(i)
            visited[i] = True
            recursive(i)
            answer.pop()
            visited[i] = False

while True:
    case = list(map(int, input().split()))
    if case[0] == 0:
        break
    nums = case[1:]
    answer = []
    visited = [False for _ in range(50)]
    
    recursive(0)
    print()