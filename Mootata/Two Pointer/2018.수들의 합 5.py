n = int(input())
answer = 0

left, right = 0, 1
count = 1

while left <= right:
    if count > n:
        count -= left
        left += 1
    elif count < n:
        right += 1
        count += right
    else:
        right += 1
        count += right
        answer += 1

print(answer)