# 2565. 전깃줄

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)])
temp = []
# LIS
for a, x in arr:
    if not temp or temp[-1] < x:
        temp.append(x)
    else:
        idx = bisect_left(temp, x)
        temp[idx] = x

print(n-len(temp))
