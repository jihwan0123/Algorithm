# 9095. 1,2,3 더하기

import sys
input = sys.stdin.readline

t = int(input())

nums = [int(input()) for _ in range(t)]
dp = [0] * (max(nums)+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max(nums)+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for n in nums:
    print(dp[n])
