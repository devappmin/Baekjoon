import sys

statement = sys.stdin.readline().rstrip()

while statement != '#':
    statement = statement.lower()
    total = 0

    for c in ['a', 'e', 'i', 'o', 'u']:
        total += statement.count(c)

    print(total)
    statement = sys.stdin.readline().rstrip()