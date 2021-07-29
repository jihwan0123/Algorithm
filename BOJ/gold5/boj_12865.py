# 12865. 평범한 배낭

import sys
input = sys.stdin.readline


n, k = map(int, input().split())
values = [list(map(int, input().split())) for _ in range(n)]  # (무게w, 가치v)

dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= values[i-1][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-values[i-1][0]] + values[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])
