from itertools import permutations

n = int(input())
nums = list(permutations((1, 2, 3, 4, 5, 6, 7, 8, 9), 3))

for _ in range(n):
    num, s, b = map(int, input().split())
    r = 0
    num = list(map(int, str(num)))
    
    for i in range(len(nums)):
        s_count, b_count = 0, 0
        i -= r
        
        for j in range(3):
            if num[j] in nums[i]:
                if j == nums[i].index(num[j]):
                    s_count += 1
                else:
                    b_count += 1
        if s_count != s or b_count != b:
            nums.remove(nums[i])
            r += 1
print(len(nums))

# 숫자 3개로 만들 수 있는 모든 경우의 수를 담은 리스트를 만들고,
# 입력된 값들과 해당 리스트에 있는 값의 스트라이크, 볼 개수를 비교함.
# 스트라이크, 볼 개수가 같아야 후보에 들어갈 수 있음.