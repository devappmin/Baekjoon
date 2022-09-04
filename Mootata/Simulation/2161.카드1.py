from collections import deque

cards = deque([i for i in range(1, int(input()) + 1)])
throw = []

while len(cards) > 1:
    throw.append(cards.popleft())
    cards.append(cards.popleft())

print(*(throw + list(cards)))