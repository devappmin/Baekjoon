n, m = map(int, input().split())
arr = [input()[::-1] for _ in range(n)]
print(*arr, sep='\n')
