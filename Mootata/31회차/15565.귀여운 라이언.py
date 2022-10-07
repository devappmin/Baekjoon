n, k = map(int, input().split())
dolls = list(map(int, input().split()))
results = []
count = 0
l = 0

left, right = 0, 0

while left <= right <= n:
    if count < k:
        if right < n:
            if dolls[right] == 1:
                count += 1
            right += 1
            l += 1
        else:
            break
            
    else:
        results.append(l)
        if dolls[left] == 1:
            count -= 1
        left += 1
        l -= 1
        

if results:
    print(min(results))
else:
    print(-1)