# 1965. 상자넣기

n = int(input())
sizes = list(map(int, input().split()))
dp = [1]*(n+1)

for i in range(1, n):
    for j in range(i): # 앞에 있는 상자들과 비교
        if sizes[i] > sizes[j]: # 앞의 값보다 크면
            dp[i] = max(dp[i], dp[j]+1) # i번째 값과 j번째값에 1더한값 중 큰값 저장

print(max(dp))
