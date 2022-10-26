a, b, c = map(int, input().split())

if len(set([a, b, c])) == 1:
    print(10000 + a * 1000)
    exit()

if len(set([a, b, c])) == 2:
    if a == b or a == c:
        print(1000 + a * 100)
        exit()

    print(1000 + b * 100)
    exit()

print(sorted([ a, b, c ])[-1] * 100)
