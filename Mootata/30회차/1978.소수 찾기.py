n = int(input())
numbers = list(map(int, input().split()))
answer = 0

for num in numbers:
    flag = True
    
    if num == 1:
        continue
    
    for i in range(2, num):
        if num % i == 0:
            flag = not flag
            break
    
    if flag:
        answer += 1

print(answer)