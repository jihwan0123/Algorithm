# 1806. 부분합

import sys
input = sys.stdin.readline
MAX_NUM = sys.maxsize

n, s = map(int, input().split())
nums = list(map(int, input().split()))

l = r = total = 0
ans = MAX_NUM
while r < n or total > s:
    if total >= s:
        total -= nums[l]
        l += 1
    else:
        total += nums[r]
        r += 1

    if total >= s:
        ans = min(ans, r - l)


if ans == MAX_NUM:
    print(0)
else:
    print(ans)

# 5 11
# 1 2 3 4 5
