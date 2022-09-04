n = int(input())
people = list(map(int, input().split()))
line = [0 for _ in range(n)]

for i in range(1, n + 1):
    count = 0
    for j in range(n):
        if count == people[i - 1] and line[j] == 0:
            line[j] = i
            break
        elif line[j] == 0:
            count += 1

print(*line)