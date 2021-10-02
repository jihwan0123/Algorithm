# 2294. 동전 2

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
dp = [100001] * (k + 1)

for coin in coins:
    if coin > k:
        break
    dp[coin] = 1
    for i in range(coin+1, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)


print(dp[k] if dp[k] < 100001 else -1)
