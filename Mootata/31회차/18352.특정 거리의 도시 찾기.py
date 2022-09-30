from collections import deque

n, m, k, x = map(int, input().split())
roads = [[] for _ in range(n + 1)]
result = []

for i in range(m):
    a, b = map(int, input().split())
    roads[a].append(b)

def dijkstra(n, x):
    q = deque()
    q.append(x)
    weights = [float('inf') for _ in range(n + 1)]
    weights[x] = 0
    
    while q:
        node = q.popleft()
        
        for n in roads[node]:
            if weights[n] <= weights[node] + 1:
                continue
            
            weights[n] = weights[node] + 1
            q.append(n)
    return weights

result = dijkstra(n, x)

if k in result:
    for i in range(n + 1):
        if result[i] == k:
            print(i)
else:
    print(-1)