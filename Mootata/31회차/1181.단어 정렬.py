import sys

input = sys.stdin.readline

words = set()

for n in range(int(input())):
    words.add(input())

answer = sorted(list(words), key = lambda x: (len(x), x))

print(''.join(answer))