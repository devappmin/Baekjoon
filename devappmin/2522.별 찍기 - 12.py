n = int(input())

for idx in range(1, n + 1):
    print(' ' * (n - idx) + '*' * idx)

for idx in range(1, n):
    print(' ' * idx + '*' * (n - idx))