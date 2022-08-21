scores = []
for _ in range(5):
    t = int(input())
    scores.append(t if t >= 40 else 40)

print(sum(scores) // 5)
