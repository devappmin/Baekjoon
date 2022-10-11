n = int(input())

for h in range(n):
    print(' ' * (n - h - 1) + '*' * (h * 2 + 1))

for h in range(1, n):
    print(' ' * h + '*' * ((n - h) * 2 - 1))
