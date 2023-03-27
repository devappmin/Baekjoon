n=int(input())
a,b,c=map(int,input().split())
print(sum([min(a,n),min(b,n),min(c,n)]))
