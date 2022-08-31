from math import prod

val = str(prod([int(input()) for _ in range(3)]))
arr = [0] * 10

for t in val:
    arr[int(t)] += 1

print(*arr, sep="\n")
