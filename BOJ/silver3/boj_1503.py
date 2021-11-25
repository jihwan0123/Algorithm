# 1503. 세 수 고르기

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
used = [0] * 1002
nums = list(map(int, input().split()))
for i in nums:
    used[i] = 1

ans = 1e9
for x in range(1, 1001):
    if used[x]:
        continue
    for y in range(x, 1001):
        if used[y]:
            continue
        for z in range(y, 1002):
            if used[z]:
                continue
            temp = x * y * z
            ans = min(ans, abs(n-temp))
            if n+1 < temp:
                break
print(ans)
