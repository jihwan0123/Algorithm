# 14002. 가장 긴 증가하는 부분수열 4

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [0] * n
ans = 0
for i in range(n):  # num 전체 돌면서
    maxV = 0  # max값 초기화
    for j in range(i+1):  # i보다 앞의 값중에서
        if nums[j] < nums[i]:  # 작은값이 있으면
            maxV = max(maxV, dp[j])  # 작은값의 dp값 최댓값에 저장

    dp[i] = 1 + maxV  # 최댓값 + 1이 i번째 사용해서 만들 수 있는 가장 긴 부분수열 길이
    ans = max(ans, dp[i])  # 정답에 최댓값 갱신

print(ans)
res = []
for i in range(n-1,-1,-1):
    if dp[i] == ans:
        res.append(nums[i])
        ans -= 1
        if not ans:
            break

print(*res[::-1])