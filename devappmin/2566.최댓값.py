arr = [list(map(int, input().split())) for _ in range(9)]

m,y,x = arr[0][0],0,0

for i in range(9):
    for j in range(9):
        if arr[i][j] > m:
            m,y,x = arr[i][j],i,j
print("{}\n{} {}".format(m,y + 1,x + 1))
