from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))
dic = defaultdict(int)
answer = 0
count = 0

left, right = 0, 0

while right < n:
    if dic[nums[right]] < k:
        dic[nums[right]] += 1
        count += 1
        right += 1
    else:
        dic[nums[left]] -= 1
        answer = max(answer, count)
        count -= 1
        left += 1

print(max(answer, count))