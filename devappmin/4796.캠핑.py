import sys

test_case = 1
while True:
    l, p, v = map(int, sys.stdin.readline().split())

    if not l and not p and not v:
        break

    m = ( v // p ) * l
    print("Case {}: {}".format(test_case, m + min(( v % p ), l)))
    test_case += 1


