import sys

a = sys.stdin.readline().rstrip()
b = list(sys.stdin.readline().split())

for c in b:
    a = a.replace(c, c.lower())

print(a)
