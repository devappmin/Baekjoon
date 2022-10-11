for t in range(int(input())):
    inputs = list(input().split())
    count = int(inputs[0])
    string = list(inputs[1])
    answer = ''
    
    for i in range(len(string)):
        answer += string[i] * count
    
    print(answer)