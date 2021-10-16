# 1932. 정수 삼각형

import sys
input = sys.stdin.readline

n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = nums[0][0]
for i in range(1, n):
    for j in range(len(nums[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + nums[i][j]
        elif j == len(nums[i]):
            dp[i][j] = dp[i-1][j-1] + nums[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + nums[i][j]

print(max(dp[n-1]))
