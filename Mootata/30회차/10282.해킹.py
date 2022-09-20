from heapq import heappop, heappush

def dijkstra():
    global answer
    pq = []
    heappush(pq, (0, c))
    weights[c] = 0
    
    while pq:
        time, comp = heappop(pq)
        answer.add(comp)
        
        if time > weights[comp]:
            continue
        
        for t, nc in computers[comp]:
            nt = time + t
            
            if nt < weights[nc]:
                weights[nc] = nt
                heappush(pq, (nt, nc))
    return answer

for t in range(int(input())):
    n, d, c = map(int, input().split())
    computers = [[] for _ in range(n + 1)]
    weights = [float("inf") for _ in range(n + 1)]
    answer = set()
    count = 0
    
    for i in range(d):
        a, b, s = map(int, input().split())
        computers[b].append((s, a))
    
    hacked = dijkstra()
    highest = 0
    
    for i in hacked:
        if weights[i] != float('inf'):
            highest = max(highest, weights[i])
    
    print(len(hacked), highest)