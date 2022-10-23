n = [0, 0]
for i in range(5):
    s = sum(map(int, input().split()))
    if n[1] < s:
        n = [i + 1, s]
print(*n)
