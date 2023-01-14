from collections import deque

n = int(input())
m = int(input())
friends = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

def bfs():
    q = deque()
    q.append((1, 0))
    visited[1] = True
    count = 0
    
    while q:
        x, dist = q.popleft()
        if dist <= 2:
            count += 1
            
        for i in friends[x]:
            if not visited[i]:
                q.append((i, dist + 1))
                visited[i] = True


    return count - 1

print(bfs())