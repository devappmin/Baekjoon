import sys

a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print('Error')
    exit(0)

if a == b == c:
    print('Equilateral')
    exit(0)

if len(set([a, b, c])) == 2:
    print('Isosceles')
    exit(0)

print('Scalene')
