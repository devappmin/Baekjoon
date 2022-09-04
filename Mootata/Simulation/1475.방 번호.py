from collections import Counter
from math import ceil

n = list(map(int, input().replace('9', '6')))
count = Counter(n)

if 6 in count:
    count[6] = ceil(count[6] / 2)

print(max(count.values()))