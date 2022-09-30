n, m = map(int, input().split())
nums = []
answer = float('inf')

for _ in range(n):
    num = int(input())
    nums.append(num)

nums.sort()
left, right = 0, 1

while right < n:
    s = abs(nums[left] - nums[right])
    if s > m:
        answer = min(answer, s)
        left += 1
    elif s < m:
        right += 1
    else:
        print(s)
        exit(0)

print(answer)