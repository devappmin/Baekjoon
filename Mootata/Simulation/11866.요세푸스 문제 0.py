n, k = map(int, input().split())
answer = []
numbers = [i for i in range(1, n + 1)]
idx = 0

while numbers:
    idx += (k - 1)
    if idx > len(numbers) - 1:
        idx %= len(numbers)
    answer.append(numbers.pop(idx))

print('<', str(answer)[1:-1], '>', sep = '')