import sys

INF = float('inf')

n = int(sys.stdin.readline())
h = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = INF

for first_value in range(3):
    dp = [[INF, INF, INF] for _ in range(n)]
    dp[0][first_value] = h[0][first_value]

    for idx in range(1, n):
        dp[idx] = [ h[idx][0] + min(dp[idx - 1][1], dp[idx - 1][2]),
                    h[idx][1] + min(dp[idx - 1][0], dp[idx - 1][2]),
                    h[idx][2] + min(dp[idx - 1][0], dp[idx - 1][1])]
    
    for i in range(3):
        if i != first_value:
            answer = min(answer, dp[-1][i])

print(answer)