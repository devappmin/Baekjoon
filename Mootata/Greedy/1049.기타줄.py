n, m = map(int, input().split()) # 끊어진 기타줄 수 n, 브랜드 수 m
brands = []

for i in range(m):
    brands.append(list(map(int, input().split())))

six = min(brands, key = lambda x: x[0])[0]
one = min(brands, key = lambda x: x[1])[1]

print(min((six * (n // 6)) + (one * (n % 6)), six * ((n // 6) + 1), one * n)) # 세트 + 단품, 세트, 단품