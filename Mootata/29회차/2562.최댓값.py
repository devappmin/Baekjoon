nums = []

for _ in range(9):
    nums.append(int(input()))

answer = max(nums)

print(answer, nums.index(answer) + 1)