n = int(input())

for h in range(1, n):
    print('*' * h, ' ' * (n - h - 1) * 2, '*' * h)
print('*' * ( n * 2 ))
for h in range(n - 1, 0, -1):
    print('*' * h, ' ' * (n - h - 1) * 2, '*' * h)
