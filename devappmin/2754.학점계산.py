import sys

n, m = map(int, sys.stdin.readline().split())

arr1 = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr2 = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(arr1[i][j] + arr2[i][j], end=" ")
    print()