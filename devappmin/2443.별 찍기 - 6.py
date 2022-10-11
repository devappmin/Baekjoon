n = int(input())
for h in range(n):
    print(" " * h, "*" * ((n - h) * 2 - 1), sep='')

