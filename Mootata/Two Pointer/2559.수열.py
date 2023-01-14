n, k = map(int, input().split())
t = list(map(int, input().split()))
answer = -float('inf')
left, right = 0, k - 1
sub_sum = sum(t[left:right + 1])

while right < n:
    answer = max(answer, sub_sum)
    sub_sum -= t[left]
    left += 1
    right += 1
    if right < n:
        sub_sum += t[right]

print(answer)