from collections import deque

n, m = map(int, input().split())
q = deque(i for i in range(1, n + 1))
numbers = map(int, input().split())
answer = 0

for num in numbers:
    idx = q.index(num)
    l = len(q) // 2
    while True:
        if q[0] == num:
            q.popleft()
            break
        else:
            if idx > l:
                q.rotate(1)
                answer += 1
            else:
                q.rotate(-1)
                answer += 1

print(answer)