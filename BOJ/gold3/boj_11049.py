# 11049. 행렬 곱셈 순서

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for j in range(1, n):
    for i in range(n-j):
        # 2개씩 곱한거부터 n개 곱한거 순서대로 계산
        start, end = i, i+j
        dp[start][end] = sys.maxsize
        # start 부터 end까지 곱했을때 최솟값
        for k in range(start, end):
            x = min(dp[start][end],
                    dp[start][k] + dp[k+1][end] +
                    arr[start][0] * arr[k][1] * arr[end][1])
            dp[start][end] = x

            # for d in dp:
            #     print(*d)
            # print()

print(dp[0][-1])
