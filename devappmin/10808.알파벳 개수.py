from collections import defaultdict

dicts = defaultdict(int)
for c in input():
    dicts[c] += 1
    
for c in 'abcdefghijklmnopqrstuvwxyz':
    print(dicts[c], end=' ')
