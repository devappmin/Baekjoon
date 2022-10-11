from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robots = deque([0 for _ in range(n)])
answer = 1

while belt.count(0) < k:
    belt.rotate()
    robots.rotate()
    robots[-1] = 0
    
    for i in range(n - 2, -1, -1): # 가장 먼저 올라간 로봇부터 이동
        if robots[i] and not robots[i + 1] and belt[i + 1]:  # 해당 칸에 로봇이 없고, 내구도 1 이상
            belt[i + 1] -= 1 # 내구도 깎고
            robots[i], robots[i + 1] = 0, robots[i] # 로봇 앞으로 이동
    robots[n - 1] = 0
    
    if not robots[0] and belt[0]: # 올리는 위치에 로봇 없고, 내구도 0 아니면 올림
        robots[0] = 1
        belt[0] -= 1
    
    answer += 1

print(answer)