n = input()
if len(n) == 1:
    n = '0' + n

answer = n
i = 0

while True:
    n = n[-1] + str(int(n[0]) + int(n[1]))[-1]
    i += 1

    if n == answer:
        break

print(i)
