import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    a %= 10

    if a == 0:
        print(10)
        continue

    if a in [1, 5, 6]:
        print(a)
        continue

    if a in [4, 9]:
        if b % 2 == 1:
            print(a)
        else:
            print((a * a) % 10)

        continue

    b %= 4
    if not b:
        print((a ** 4) % 10 % 10 % 10)
        continue

    print((a ** b) % 10 % 10 % 10)
