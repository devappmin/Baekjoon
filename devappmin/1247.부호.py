for _ in range(3):
    n = int(input())
    value = sum(list(map(int, [input() for _ in range(n)])))
    print(0 if value == 0 else '+' if value > 0 else '-')
    
