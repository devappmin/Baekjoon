s,k,h=map(int,input().split())
d={s:"Soongsil",k:"Korea",h:"Hanyang"}
print("OK"if s+k+h>=100 else d[min([s,k,h])])
