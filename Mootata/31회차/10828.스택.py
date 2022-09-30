stack = []

for n in range(int(input())):
    cmd, num = input().split()
    num = int(num)
    
    if cmd == 'push':
        stack.append(num)
    elif cmd == 'pop':
        if cmd:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if cmd:
            print(0)
        else:
            print(1)
    else:
        if cmd:
            print(stack[-1])
        else:
            print(-1)