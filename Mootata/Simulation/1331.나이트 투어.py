path = [list(input()) for _ in range(36)]
visited = [[False for _ in range(7)] for _ in range(7)]
flag = True

for idx, p in enumerate(path):
    x, y = p[0], int(p[1])
    if idx == 35:
        if not visited[ord(x) - 64][y] and abs(ord(x) - ord(path[0][0])) == 2 and abs(y - int(path[0][1])) == 1:
            visited[ord(x) - 64][y] = True
            continue
        elif not visited[ord(x) - 64][y] and abs(ord(x) - ord(path[0][0])) == 1 and abs(y - int(path[0][1])) == 2:
            visited[ord(x) - 64][y] = True
            continue
        else:
            flag = False
            break
    else:
        if not visited[ord(x) - 64][y] and abs(ord(x) - ord(path[idx + 1][0])) == 2 and abs(y - int(path[idx + 1][1])) == 1:
            visited[ord(x) - 64][y] = True
            continue
        elif not visited[ord(x) - 64][y] and abs(ord(x) - ord(path[idx + 1][0])) == 1 and abs(y - int(path[idx + 1][1])) == 2:
            visited[ord(x) - 64][y] = True
            continue
        else:
            flag = False
            break

if flag:
    print("Valid")
else:
    print("Invalid")