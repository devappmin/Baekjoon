from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))


left, right = 0, 1

while True:
    if nums[left] 