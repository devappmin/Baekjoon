n = int(input())

for h in range(n):
    print(' ' * h, '*' * ((n - h) * 2 - 1), sep='')

for h in range(n - 2, -1, -1):
    print(' ' * h, '*' * ((n - h) * 2 - 1), sep='')