import sys

n = int(input())
users = []
for _ in range(n):
    age, name = input().split()
    age = int(age)
    users.append((age, name))

users = sorted(users, key=lambda a: a[0])

for user in users:
    print(*user)
