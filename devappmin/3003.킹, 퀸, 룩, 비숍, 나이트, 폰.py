t = [1, 1, 2, 2, 2, 8]
l = list(map(int, input().split()))

for idx in range(6):
    t[idx] -= l[idx]

print(*t)