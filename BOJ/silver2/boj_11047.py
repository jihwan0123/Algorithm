# 11047. 동전 0

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [1] + [int(input()) for _ in range(n)]

ans = 0
i = n
while i:
    if k == 0:
        break
    ans += k//arr[i]
    k %= arr[i]
    i -= 1

print(ans)