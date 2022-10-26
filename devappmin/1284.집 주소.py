from collections import defaultdict

dicts = defaultdict(lambda: 3)
dicts['1'] = 2
dicts['0'] = 4

n = input()
while n != '0':
    print(sum([1, *[dicts[x] + 1 for x in list(n)]]))
    n = input()
