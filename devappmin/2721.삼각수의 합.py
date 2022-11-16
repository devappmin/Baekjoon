for _ in range(int(input())):print(sum(x*sum(y for y in range(1,x+2))for x in range(1,int(input())+1)))
