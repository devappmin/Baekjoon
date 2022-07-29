n, m = map(int, input().split()) # 배열A, B의 크기 N, M

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*sorted(a + b))