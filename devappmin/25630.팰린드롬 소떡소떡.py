from math import ceil

n = int(input())
st = input()
answer = 0

for idx in range(ceil(n / 2)):
    if st[idx] != st[n - idx - 1]:
        answer += 1

print(answer)
