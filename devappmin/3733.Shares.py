while True:
    try: n, m = map(int, input().split())
    except: break
    print(m // (n + 1))
