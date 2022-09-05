from collections import deque

n = int(input())
a, b = map(int, input().split())
family = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for i in range(int(input())):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

def bfs():
    q = deque()
    q.append((a, 0))
    
    while q:
        current, count = q.popleft()
        if current == b:
            return count
        if not visited[current]:
            for i in family[current]:
                q.append((i, count + 1))
                visited[current] = True
    return -1

print(bfs())