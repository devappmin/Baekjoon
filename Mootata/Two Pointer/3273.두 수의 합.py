n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
answer = 0
left, right = 0, n - 1

while left < right:
    temp = nums[left] + nums[right]
    if temp == x:
        left += 1
        answer += 1
    elif temp > x:
        right -= 1
    else:
        left += 1

print(answer)