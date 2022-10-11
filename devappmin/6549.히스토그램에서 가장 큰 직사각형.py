import sys

def solution(n, arr):
    histogram = [0] + arr + [0]
    checked = [0]
    area = 0

    for i in range(1, n + 2):
        # 저장된 높이보다 현재 높이가 낮을 경우, while에 진입하며
        # 이전에 저장된 area (저장된 높이에서의 area)와 현재의 area를 비교한다.
        # 두 값 중 큰 값이 새로운 area에 저장되게 된다.
        while checked and histogram[checked[-1]] > histogram[i]:
            current = checked.pop()
            area = max(area, (i - 1 - checked[-1]) * histogram[current])
        checked.append(i)
    print(area)

while True:
    n, *arr = map(int, sys.stdin.readline().split())

    if n == 0:
        break

    solution(n, arr)
