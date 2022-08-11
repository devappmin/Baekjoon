n = int(input())
if n == 1:
    print(0)
    exit(0)

nums = []
is_prime = [False, False] + [True] * (n - 1)

for idx in range(2, n + 1):
    if is_prime[idx]:
        nums.append(idx)

        for i in range(idx * 2, n + 1, idx):
            is_prime[i] = False

left, right = 0, 0 
total = nums[0]
answer = 0

while left <= right:
    if total == n:
        answer += 1

    if total > n or right == len(nums) - 1:
        total -= nums[left]
        left += 1
        continue
    
    right += 1
    total += nums[right]

print(answer)