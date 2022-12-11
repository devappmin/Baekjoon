a, b, c = sorted(list(map(int, input().split())))

while not (a == 0 and b == 0 and c == 0):
    is_right = (a ** 2 + b ** 2) ** (1 / 2) == c
    print('right' if is_right else 'wrong')
    a, b, c = sorted(list(map(int, input().split())))
