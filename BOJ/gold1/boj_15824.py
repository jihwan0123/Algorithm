# 15824. 너 봄에는 캡사이신이 맛있단다.

import sys
input = sys.stdin.readline
MOD = 1000000007

n = int(input())
taste = [0]+sorted(list(map(int, input().split())))
exps = [1]
for i in range(1, n+1):
    exps.append((exps[i-1]*2) % MOD)

ans = 0
for i in range(1, n+1):
    ans += (exps[i-1]-exps[n-i])*taste[i]

print(ans % MOD)
