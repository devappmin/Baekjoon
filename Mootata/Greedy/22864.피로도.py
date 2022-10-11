a, b, c, m = map(int, input().split())

stress = 0
time = 0
answer = 0

if a > m:
    print(0)
else:
    while time != 24:
        time += 1
        
        if stress + a <= m:
            answer += b
            stress += a
        else:
            if stress - c >= 0:
                stress -= c
            else:
                stress = 0
    
    print(answer)