import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
lis = [0]

for num in nums:
    if lis[-1] < num:
        lis.append(num)
        continue

    left = 0
    right = len(lis)

    while left < right:
        center = (left + right) // 2

        if lis[center] < num:
            left = center + 1
        else:
            right = center
        
    lis[right] = num
    
print(len(lis) - 1)