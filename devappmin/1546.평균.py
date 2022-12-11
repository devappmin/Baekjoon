n = int(input())
nums = list(map(int, input().split()))
new_nums = [x / max(nums) * 100 for x in nums]
print(sum(new_nums) / n)
