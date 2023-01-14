from collections import deque

n = int(input())
balloons = deque(enumerate(map(int, input().split())))
answer = []

while balloons:
    idx, next_balloon = balloons.popleft()
    answer.append(idx + 1)
    
    if next_balloon > 0:
        balloons.rotate(-(next_balloon - 1))
    elif next_balloon < 0:
        balloons.rotate(-next_balloon)

print(*answer, sep = ' ')