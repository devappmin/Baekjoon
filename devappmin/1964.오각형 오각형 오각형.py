n = int(input())
dot, inc = 5, 7
for idx in range(1, n):
    dot += inc
    inc += 3
print(dot % 45678)
