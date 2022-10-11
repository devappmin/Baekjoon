from collections import deque

n = int(input())
cards = deque(i for i in range(1, n + 1))

for i in range(n - 1):
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])