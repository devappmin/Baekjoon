import sys

n, k = map(int, sys.stdin.readline().split())
scores = sorted(list(map(int, sys.stdin.readline().split())), key=lambda a: -a)
print(scores[k - 1])
