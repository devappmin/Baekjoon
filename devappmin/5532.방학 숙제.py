import sys
from math import ceil

l = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())

print(l - max(ceil(b / d), ceil(a / c)))
