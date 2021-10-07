# 1817. 짐 챙기는 숌

import sys

n, m = map(int, input().split())
if n == 0:
    print(0)
    sys.exit()

weights = list(map(int, input().split()))

s = 0
cnt = 1
for i in range(n-1, -1, -1):
    s += weights[i]
    if s > m:
        cnt += 1
        s = weights[i]

print(cnt)
