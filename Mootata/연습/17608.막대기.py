n = int(input())
stack = []

for _ in range(n):
    stack.append(int(input()))

pre = stack[-1]
count = 1

for i in range(n - 1, -1, -1):
    if stack[i] > pre:
        count += 1
        pre = stack[i]

print(count)