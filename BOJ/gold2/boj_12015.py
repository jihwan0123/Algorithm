# 12015. 가장 긴 증가하는 부분수열2

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

ans = [nums[0]]

for num in nums:
    if num > ans[-1]:
        ans.append(num)
    elif num == ans[-1]:
        continue
    else:
        idx = bisect_left(ans, num)
        ans[idx] = min(num, ans[idx])

print(len(ans))
