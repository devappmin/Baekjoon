d,p=0,0
for _ in range(int(input())):
    if abs(d - p) > 1:
        break

    if input() == 'D':
        d += 1
    else:
        p += 1

print("{}:{}".format(d,p))
