# 14501. 퇴사

import sys
input = sys.stdin.readline

## DFS
# def dfs(cur, total):
#     global ans
#     if cur > n-1:
#         ans = max(ans, total)
#         return

#     dfs(cur + 1, total)
#     if cur + tp[cur][0] <= n:
#         dfs(cur + tp[cur][0], total + tp[cur][1])


# n = int(input())
# tp = [list(map(int, input().split())) for _ in range(n)]

# ans = 0
# dfs(0, 0)
# print(ans)


## DP
n = int(input())
tp = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n+1)
for i in range(n):
    if i + tp[i][0] <= n: # n번째를 넘어가지 않는 것만 계산 : index error 방지
        # 상담을 했을때 더한값과 기존값 중 최댓값으로 갱신
        dp[i + tp[i][0]] = max(dp[i+tp[i][0]], dp[i] + tp[i][1])
    dp[i + 1] = max(dp[i], dp[i+1]) # 상담 없이 다음날로 이동하는경우 최댓값 갱신
# dp값중 최댓값 출력
print(max(dp))
