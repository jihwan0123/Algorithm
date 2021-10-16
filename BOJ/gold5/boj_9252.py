# 9252. LCS 2

a = input()
b = input()
dp = [[''] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]: # 같으면
            # 앞의 값에 이어붙인다.
            dp[i+1][j+1] = dp[i][j] + a[i]
        else: # 다르면
            # 앞에서 더 긴 값 가져온다.
            dp[i+1][j+1] = dp[i][j+1] if len(dp[i][j+1]) > len(dp[i+1][j]) else dp[i+1][j]

if not dp[-1][-1]:
    print(0)

else:
    print(len(dp[-1][-1]))
    print(dp[-1][-1])
