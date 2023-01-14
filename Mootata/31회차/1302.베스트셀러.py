from collections import defaultdict

n = int(input())
books = defaultdict(int)
answer = []

for i in range(n):
    books[input()] += 1

m = max(books.values())

for k, v in books.items():
    if v == m:
        answer.append(k)

print(sorted(answer)[0])