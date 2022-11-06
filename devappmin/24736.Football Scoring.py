t = [6,3,2,1,2]
k = lambda: sum(t[x] * v for x, v in enumerate(map(int, input().split())))
print(k(), k())
