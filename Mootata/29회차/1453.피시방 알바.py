_ = int(input())
PC_Georgia = list(map(int, input().split()))        
sits = [0 for _ in range(101)]
refused = 0

for i in PC_Georgia:
    if sits[i] != 0:
        refused += 1
    else:
        sits[i] += 1

print(refused)