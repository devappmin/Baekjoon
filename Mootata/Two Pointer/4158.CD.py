while True:
    n, m = map(int, input().split())
    sang = []
    sun = []
    answer = 0
    
    if n == m == 0:
        break
    
    for i in range(n):
        sang.append(int(input()))

    for i in range(m):
        sun.append(int(input()))

    left, right = 0, 0

    while left < n and right < m:
        if sang[left] == sun[right]:
            answer += 1
            left += 1
            right += 1
        elif sang[left] > sun[right]:
            right += 1
        else:
            left += 1

    print(answer)