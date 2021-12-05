# 2193. 이친수

import sys
input = sys.stdin.readline

n = int(input())
# (0, 1) : 0으로 끝나는 경우, 1로 끝나는 경우
dp = [[0, 0] for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = 1

for i in range(2, n+1):
    # 0은 0 or 1 모두 가능
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    # 1은 무조건 0 다음에만 올 수 있음
    dp[i][1] = dp[i-1][0]

print(sum(dp[n]))
