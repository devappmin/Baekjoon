n, k = map(int, input().split())
blocks = list(map(int, input().split()))
jump = True
last_jump = 0
left, right = 0, 0
answer = 0

while right < n - 1:
    if blocks[right] <= k:
        right += 1
    else:
        if jump:
            last_jump = right
            right += 1
            jump = False
        else:
            answer = max(answer, right - left + 1)
            left = last_jump + 1
            jump = True
            
            if len(blocks) - left <= answer:
                break

print(max(answer, right - left + 1))