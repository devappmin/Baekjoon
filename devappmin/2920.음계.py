v = list(map(int,input().split()))
print("ascending" if v == sorted(v) else "descending" if v == sorted(v, key=lambda a: -a) else "mixed")
