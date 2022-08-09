import sys

def binary_search(left, right, target):
    while left < right:
        mid = (left + right) // 2
        if lis[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

lis = [numbers[0], ]
index_value = [[0, 0] for _ in range(n)]
index_value[0][1] = numbers[0]

for i in range(1, n):
    index_value[i][1] = numbers[i]
    if lis[-1] < numbers[i]:
        index_value[i][0] = len(lis)
        lis.append(numbers[i])
    else:
        idx = binary_search(0, len(lis)-1, numbers[i])
        index_value[i][0] = idx
        lis[idx] = numbers[i]

idx = len(lis) - 1
answer = []

for i in range(n-1, -1, -1):
    if idx == -1:
        break

    if idx == index_value[i][0]:
        answer.append(index_value[i][1])
        idx -= 1

print(len(answer))
print(*answer[::-1])