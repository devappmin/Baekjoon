def sol1():
    word = list(input())
    ca = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    stack = [word[0]]
    answer = len(word)
    
    for c in word[1:]:
        if c == '=' or c == '-'or c == 'j':
            if len(stack) >= 2 and stack[-2] + stack[-1] + c in ca:
                answer -= 2
                stack = []
            elif len(stack) >= 1 and stack[-1] + c in ca:
                answer -= 1
                stack = []
        else:
            stack.append(c)
            
    print(answer)

def sol2():
    word = input()
    ca = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    
    for i in ca:
        word = word.replace(i, '.')
    print(len(word))

sol1()
sol2()