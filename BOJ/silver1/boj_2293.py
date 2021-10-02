# 2293. 동전 1

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
dp = [0] * (k + 1)

for coin in coins:
    if coin > k:
        break
    dp[coin] += 1
    for i in range(coin+1, k+1):
        dp[i] += dp[i-coin]

print(dp[k])
