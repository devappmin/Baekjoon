a, b = input().split()
a = list(map(int, a))
b = list(map(int, b))

answer = 0
for i in a:
    answer += sum([j * i for j in b])

print(answer)
