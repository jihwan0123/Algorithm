# 12852. 1로 만들기2

n = int(input())
dp = list(range(n+1))

# 우선순위 순서로 dp 갱신
for i in range(1, n+1):
    dp[i] = min(dp[i], dp[i - 1] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n]-1)
# 역순으로 체크하면서 출력
while n > 0:
    print(n, end=" ")
    if dp[n] == dp[n-1]+1:
        n -= 1
    elif n % 2 == 0 and dp[n] == dp[n//2]+1:
        n //= 2
    elif n % 3 == 0 and dp[n] == dp[n//3]+1:
        n //= 3