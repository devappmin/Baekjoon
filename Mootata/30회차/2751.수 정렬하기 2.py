n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

for i in sorted(numbers):
    print(i)