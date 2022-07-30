n, s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

def recursive(index, sub_sum):
    global answer
    if index >= n:
        return
    
    sub_sum += nums[index]
    
    if sub_sum == s:
        answer += 1
    
    recursive(index + 1, sub_sum)
    recursive(index + 1, sub_sum - nums[index])

recursive(0, 0)
print(answer)