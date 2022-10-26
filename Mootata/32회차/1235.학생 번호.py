n = int(input())
students = [input() for _ in range(n)]
cnt = 1

while True:
    if len(set(map(lambda x: x[-cnt:], students))) == n:
        print(cnt)
        break
    cnt += 1