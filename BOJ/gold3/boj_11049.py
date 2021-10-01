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
        # start 부터 end까지 곱했을때 최솟값 =
        # start ~ k 번까지의 연산 수 + k+1부터 end까지의 연산 수
        # + start[0]번 end[1]번 k번
        dp[start][end] = min([dp[start][k] + dp[k+1][end] + \
                                arr[start][0] * arr[k][1] * arr[end][1] \
                                    for k in range(start, end)])


print(dp[0][-1])
