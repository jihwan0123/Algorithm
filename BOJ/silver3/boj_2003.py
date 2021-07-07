# 2003. 수들의 합2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

l = r = cnt = total = 0
while r < n:
    if total >= m:
        total -= a[l]
        l += 1
    else:
        total += a[r]
        r += 1

    if total == m:
        cnt += 1

print(cnt)
