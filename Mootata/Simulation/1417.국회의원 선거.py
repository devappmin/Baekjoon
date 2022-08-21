from collections import deque
from heapq import heappop, heappush

def sol1():
    candidates = deque()
    heapq = []
    b = float('inf')
    answer = 0

    for _ in range(int(input())):
        candidates.append(int(input()))

    if len(candidates) > 1:
        d = candidates.popleft()
    else:
        return 0

    for i in candidates:
        heappush(heapq, -i)

    while True:
        b = -heappop(heapq)
        if d <= b:
            d += 1
            answer += 1
            b -= 1
            heappush(heapq, -b)
        else:
            return answer

def sol2():
    n = int(input())
    candidates = deque([int(input()) for _ in range(n)])
    d = candidates.popleft()
    answer = 0
    
    while d <= max(candidates):
        candidates[candidates.index(max(candidates))] -= 1
        d += 1
        answer += 1
    return answer

print(sol2())