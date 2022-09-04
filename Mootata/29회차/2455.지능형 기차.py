answer = 0
count = 0

for i in range(4):
    n, m = map(int, input().split())
    count -= n
    count += m
    answer = max(answer, count)

print(answer)