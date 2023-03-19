import sys
from collections import defaultdict

n = int(sys.stdin.readline())
ans = 0

for _ in range(n):
    t = sys.stdin.readline().rstrip()
    visited = defaultdict(bool)
    is_ans = True
    last = ''

    for c in t:
        if last == c:
            continue
        
        if visited[c]:
            is_ans = False
            break

        last = c
        visited[c] = True

    if is_ans:
        ans += 1

print(ans)
