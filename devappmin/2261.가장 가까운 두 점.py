import sys

n = int(sys.stdin.readline())
sorted_location = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(n)])
get_dist = lambda a, b: (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def solution(l, r):
    if l == r:
        return float('inf')

    m = (l + r) // 2
    min_dist = min(solution(l, m), solution(m + 1, r))
    target_list = []
    
    for i in range(m, l - 1, -1):
        if (sorted_location[i][0] - sorted_location[m][0]) ** 2 >= min_dist:
            break
        
        target_list.append(sorted_location[i])

    for j in range(m + 1, r + 1):
        if (sorted_location[j][0] - sorted_location[m][0]) ** 2 >= min_dist:
            break

        target_list.append(sorted_location[j])
            
    target_list.sort(key=lambda x: x[1])

    for i in range(len(target_list) - 1):
        for j in range(i + 1, len(target_list)):
            if (target_list[i][1] - target_list[j][1]) ** 2 >= min_dist:
                break

            dist = get_dist(target_list[i], target_list[j])
            min_dist = min(min_dist, dist)

    return(min_dist)

if len(sorted_location) != len(set(sorted_location)):
    print(0)
    exit()

print((solution(0, len(sorted_location) - 1)))
