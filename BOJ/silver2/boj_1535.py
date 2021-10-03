# 1535. 안녕

import sys
input = sys.stdin.readline

n = int(input())
minus = list(map(int, input().split()))
plus = list(map(int, input().split()))

# n명까지 기쁨 = 0 ~ 100
# dp[i][j] = i번째 사람까지 인사했을때 얻는 기쁨
dp = [[0] * 101 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        if minus[i-1] > j: # 손실값보다 크면 인사 못하므로
            # 이전 사람까지 인사한 최대값과 동일
            dp[i][j] = dp[i - 1][j]
        else: # 인사할 수 있으면,
            # 인사 안하는 경우, 인사하는 경우 중 최댓값으로 갱신
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - minus[i-1]] + plus[i-1])


print(dp[n][99]) # 기쁨은 100보다 작아야 하므로 99번째값 출력
