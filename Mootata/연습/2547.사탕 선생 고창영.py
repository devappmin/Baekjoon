for t in range(int(input())):
    _ = input()
    n = int(input())
    candies = []
    
    for i in range(n):
        candies.append(int(input()))
    
    if sum(candies) % n == 0:
        print("YES")
    else:
        print("NO")