n = int(input())
costs = sorted(list(list(map(int, input().split())) for _ in range(n)), key = lambda x : x[0])
answer = 0
highest = 0

for cost, fee in costs:
    m = 0
    for c, f in costs:
        if c >= cost and cost > fee:
            if cost - f > 0:
                m += cost - f
            
    if highest < m:
        answer = cost
        highest = m

print(answer)