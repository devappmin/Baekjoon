from bisect import bisect_left

def minus(n):
    return -n

n, score, p = map(int, input().split())
if n != 0:
    scores = list(map(minus, map(int, input().split())))
else:
    scores = []

answer = bisect_left(scores, -score)

if n == p and -score >= scores[p - 1]:
    print(-1)
elif answer < p:
    print(answer + 1)
else:
    print(-1)