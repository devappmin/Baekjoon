import sys
from collections import defaultdict

for _ in range(int(sys.stdin.readline())):
    m = int(sys.stdin.readline())
    money = 0
    kda = defaultdict(list)

    for idx in range(m):
        kda[idx] = tuple(map(int, sys.stdin.readline().split()))

    k_sun, d_sun, a_sun = map(int, sys.stdin.readline().split())

    for k, d, a in kda.values():
        money += max(0, k * k_sun - d * d_sun + a * a_sun)

    print(money)
