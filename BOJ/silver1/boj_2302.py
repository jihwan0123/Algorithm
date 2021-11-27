# 2302. 극장좌석

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vips = [int(input()) for _ in range(m)]
dp = [0] * (n+1)
# dp[0] = 1해야 ans 계산할 때 영향 없음
dp[0] = dp[1] = 1  # 1자리 = 1
dp[2] = 2  # 2자리 = a-b, b-a
# n번째 경우의 수
# dp[3] = 1,2 + 3, 1 + 3, 2
# dp[4] = 1,2,3 + 4, 1,2 + 4,3
# dp[5] = 1,2,3,4 + 5, 1,2,3 + 5,4
# n번째를 끝에두는 경우, 앞이랑 교환하는 경우 = n-1 + n-2
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

ans = 1
s = 0
for i in range(m):
    ans *= dp[vips[i]-s-1]
    s = vips[i]
ans *= dp[n-s]

print(ans)
