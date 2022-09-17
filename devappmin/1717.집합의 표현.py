import sys

n, m = map(int, sys.stdin.readline().split())

parent = [x for x in range(n + 1)]
rank = [0] * (n + 1)

def find(a):
    if parent[a] == a:
        return a

    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if rank[a] > rank[b]:
        parent[b] = a
        return

    parent[a] = b

    if rank[a] == rank[b]:
        rank[b] += 1


for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().split())

    if c == 0:
        union(a, b)
        continue

    a = find(a)
    b = find(b)

    print("NO" if a != b else "YES")
