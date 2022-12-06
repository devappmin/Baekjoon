for _ in range(int(input())):
    input()
    n = int(input())
    total = sum(int(input()) for _ in range(n))
    print("NO" if total % n else "YES")
