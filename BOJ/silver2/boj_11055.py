# 11055. 가장 큰 증가 부분수열

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = arr.copy()

maxV = arr[0]
# 처음부터 자기 자신보다 앞의 수까지 비교
for i in range(n):
    for j in range(i):
        # 자기 자신보다 작은 경우
        if arr[j] < arr[i]:
            # 자기 자신에 앞의 값의 DP값을 더한값과, 저장된 값 중 최댓값으로 갱신
            dp[i] = max(dp[i], dp[j] + arr[i])
    maxV = max(maxV, dp[i])

print(maxV)
