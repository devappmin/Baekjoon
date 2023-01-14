import sys

input = sys.stdin.readline

n, s = map(int, input().split())
cows = sorted([int(input()) for _ in range(n)])
cows = [i for i in cows if i < s]
answer = 0

left, right = 0, len(cows) - 1

while left < right:
    if cows[left] + cows[right] <= s:
        answer += right - left
        left += 1
    else:
        right -= 1
        
print(answer)