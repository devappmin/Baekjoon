stack = []

for n in range(int(input())):
    num = int(input())
    
    if num == 0:
        if stack:
            stack.pop()
    else:
        stack.append(num)

print(sum(stack))