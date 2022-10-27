from collections import defaultdict
d = defaultdict(int)

for s in input().upper():
    d[s] += 1

mc, mv = 0, 'A'
for k, v in d.items():
    if v > mc:
        mc, mv = v, k

cnt = 0
for _, v in d.items():
    if v == mc:
        cnt += 1

print("?" if cnt > 1 else mv)
