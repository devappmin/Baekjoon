import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

dp = [[0] * n for _ in range(n)]

# 길이가 1인 경우 자기자신인 경우 1
for idx in range(n):
    dp[idx][idx] = 1

# 길이가 2인 경우 바로 옆 인덱스의 수와 같을 경우 1
for idx in range(n - 1):
    if nums[idx] == nums[idx + 1]:
        dp[idx][idx + 1] = 1

# 길이가 3 이상인 경우 start와 end가 같은 수이고 dp[start + 1][end - 1]이 1이면(팰린드롬이면) 1
for i_idx in range(2, n):
    for j_idx in range(n - i_idx):
        if nums[j_idx] == nums[i_idx + j_idx] and dp[j_idx + 1][i_idx + j_idx - 1] == 1:
            dp[j_idx][i_idx + j_idx] = 1

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(dp[start - 1][end - 1])

# 길이가 1인 경우 자기자신인 경우 1
# 길이가 2인 경우 바로 옆 인덱스의 수와 같을 경우 1
# 길이가 3 이상인 경우 s와 e가 같은 수이고 dp[s+1][e-1]이 1이면(팰린드롬이면) 1
# 출처: https://jshong1125.tistory.com/61 [it 공부 기록용 블로그:티스토리]

# dp[a][b]에서 a와 b는 해당 값이 일치하냐를 의미한다.
# 길이가 1인 경우 두 값이 동일하므로 dp[idx][idx]의 값을 변경한다.
# 길이가 2인 경우 바로 오른쪽에 있는 값을 비교하고 두 값이 동일 할 경우 변경하는 것이기 때문에 dp[idx][idx + 1]을 특정 조건에서 발생시킨다.
# 길이가 3이상인 경우, 
# start와 end의 값이 같을 경우(j_idx와 j_idx에서 i_idx만큼 떨어진 상황)와
# start + 1(j_idx + 1)과 end - 1(j_idx에서 i_idx만큼 떨어진 곳에서 - 1)을 한 값이 1일 경우(팰린드롬일경우),
# 1로 값을 변경한다.
