n = int(input())
for h in range(n):
    print(' ' * (n - h - 1) + '*' * (h * 2 + 1))
