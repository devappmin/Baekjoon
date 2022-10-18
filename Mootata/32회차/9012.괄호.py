for n in range(int(input())):
    ps = list(input())
    stack = []
    
    for i in ps:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')