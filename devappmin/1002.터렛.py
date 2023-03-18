import sys
import math

for _ in range(int(sys.stdin.readline())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if not d and r1 == r2:
        print(-1)
        continue
    
    if abs(r1 - r2) == d or r1 + r2 == d:
        print(1)
        continue

    if abs(r1 - r2) < d < r1 + r2:
        print(2)
        continue

    print(0)
