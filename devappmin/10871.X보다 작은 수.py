import sys

n, p = map(int, sys.stdin.readline().split())
print(*[x for x in map(int, sys.stdin.readline().split()) if x < p])