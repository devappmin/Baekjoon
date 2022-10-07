n = int(input())
p = int(input())
values = [p]
discount = [500, int(p * 0.1), 2000, int(p * 0.25)]

for idx in range(1, 5):
    if idx * 5 > n:
        break
    values.append(p - discount[idx - 1])

print(max(min(values), 0))
