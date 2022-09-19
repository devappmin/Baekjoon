import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
durability = deque(map(int, sys.stdin.readline().split()))
robots = deque([0] * n)
movement = 0

while durability.count(0) < k:
    durability.rotate(1)
    robots.rotate(1)
    robots[-1] = 0

    for idx in range(n - 2, -1, -1):
        if durability[idx + 1] > 0 and not robots[idx + 1] and robots[idx]:
            robots[idx + 1] = 1
            durability[idx + 1] -= 1
            robots[idx] = 0
            
            robots[-1] = 0
    
    if durability[0] and not robots[0]:
        robots[0] = 1
        durability[0] -= 1

    movement += 1

print(movement)




# n, k = map(int, sys.stdin.readline().split())
# durability = deque(map(int, sys.stdin.readline().split()))
# robots = deque([0] * n * 2)
# robots_index = deque()
# zero_count = 0
# movement = 0

# def move():
#     global robots_index
#     durability.appendleft(durability.pop())
#     robots.appendleft(robots.pop())
#     robots_index = deque((x + 1) % (2 * n) for x in robots_index)

#     if n - 1 in robots_index:
#         robots[n - 1] = 0
#         robots_index.remove(n - 1)

# # while zero_count < k:
# for _ in range(24):
#     move()
#     temp_index = deque() 

#     for robot in robots_index:
#         next_index = (robot + 1) % (2 * n)
#         if durability[next_index] > 0 and not robots[next_index]:
#             durability[next_index] -= 1

#             if durability[next_index] == 0:
#                 zero_count += 1

#             robots[robot] = 0

#             if next_index != n - 1:
#                 robots[next_index] = 1
#                 temp_index.append(next_index)

#     print(durability, robots)
#     print(robots_index, temp_index)
#     robots_index = temp_index

#     if durability[0] and not robots[0]:
#         robots[0] = 1
#         robots_index.append(0)
#         durability[0] -= 1

#         if not durability[0]:
#             zero_count += 1

#     if n - 1 in robots_index:
#         robots[n - 1] = 0
#         robots_index.remove(n - 1)
#     movement += 1

# print(movement)