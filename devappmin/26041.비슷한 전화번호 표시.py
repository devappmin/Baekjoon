import sys

li = list(sys.stdin.readline().split())
b = sys.stdin.readline().rstrip()
answer = 0

for v in li:
    if v.startswith(b) and v != b:
        answer += 1

print(answer)
