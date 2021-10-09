# 18110. solved.ac

import sys
input = sys.stdin.readline


def round(n):
    return int(n) + (1 if n - int(n) >= 0.5 else 0)


n = int(input())
x = round(n*0.15)
nums = [int(input()) for _ in range(n)]

if n == 0:
    print(0)
    sys.exit()
if x == 0:
    print(round(sum(nums)/n))
else:
    nums.sort()
    print(round(sum(nums[x:-x])/len(nums[x:-x])))
