# 1915. 가장 큰 정사각형

import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
dp = copy.deepcopy(arr)

for i in range(1, n):
    for j in range(1, m):
        if arr[i][j]:
            # (i,j)일때 최대 길이 = 왼쪽, 위쪽, 왼쪽위대각선의 최솟값 + 1
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

print(max(map(max, dp))**2)
