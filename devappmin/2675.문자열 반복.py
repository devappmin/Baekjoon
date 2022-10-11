for _ in range(int(input())):
    n, s = input().split()
    n = int(n)
    print(*[x * n for x in s], sep='')
