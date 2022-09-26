import sys

n, l = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

paths = []

for li in graph:
    paths.append(li[:])

for idx in range(n):
    paths.append([graph[x][idx] for x in range(n)])


def stair(path):
    temp = [False] * n

    for i in range(n - 1):
        if abs(path[i] - path[i + 1]) > 1:
            return False

        if path[i] > path[i + 1]:
            for j in range(l):
                if i + 1 + j >= n or path[i + 1] != path[i + 1 + j] or temp[i + 1 + j]:
                    return False

                if path[i + 1] == path[i + 1 + j]:
                    temp[i + 1 + j] = True     
            continue

        if path[i] < path[i + 1]:
            for j in range(l):
                if i - j < 0 or path[i] != path[i - j] or temp[i - j]:
                    return False

                if path[i] == path[i - j]:
                    temp[i - j] = True   

    return True

answer = 0
for path in paths:
    if stair(path):
        answer += 1

print(answer)