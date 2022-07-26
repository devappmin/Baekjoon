import sys
from collections import defaultdict
from itertools import combinations

n = int(sys.stdin.readline())
ranks = defaultdict(int)
parents = defaultdict(set)
xs, ys, zs = [], [], []
edges = []

for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    xs.append((x, (x, y, z)))
    ys.append((y, (x, y, z)))
    zs.append((z, (x, y, z)))
    parents[(x, y, z)] = (x, y, z)
    ranks[(x, y, z)] = 0

xs = sorted(xs)
ys = sorted(ys)
zs = sorted(zs)

for star in xs, ys, zs:
    
    for idx in range(1, n):
        w1, star1 = star[idx - 1]
        w2, star2 = star[idx]
        edges.append((abs(w1 - w2), star1, star2))

def find(a):
    if parents[a] == a:
        return a

    t = find(parents[a])
    parents[a] = t

    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if ranks[a] > ranks[b]:
        parents[b] = a
        return
    
    parents[a] = b

    if ranks[a] == ranks[b]:
        ranks[b] += 1
    
def kruskal(edges):
    edges = sorted(edges, reverse=True)

    total = 0
    count = n - 1

    while count:
        weight, star1, star2 = edges.pop()

        if find(star1) == find(star2):
            continue

        union(star1, star2)
        total += weight
        count -= 1

    return total

print(kruskal(edges))