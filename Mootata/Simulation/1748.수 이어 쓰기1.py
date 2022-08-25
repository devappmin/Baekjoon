n = int(input())
l = len(str(n))
answer = 0

for i in range(l - 1):
    answer += 9 * (10 ** i) * (i + 1)

print(answer + (n - 10 ** (l - 1) + 1) * l)

# 1~9 9
# 10~99 90
# 100 ~ 999 900
# 1000~9999 9000
# 10000~99999 90000