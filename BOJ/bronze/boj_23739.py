# 23739. 벼락치기

import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums_copy = nums.copy()
ans = 0
for i in range(n-1):
    if nums[i] != nums_copy[i]:
        continue
    if nums[i] < 30:
        temp = 30
        idx = i
        while idx <= n:
            nums_copy[idx] -= temp
            if temp <= nums[idx]:
                break
            temp = abs(nums_copy[idx])
            idx += 1
    else:
        nums_copy[i] -= 30

if nums[-1] == nums_copy[-1]:
    nums_copy[-1] -= 30

for i in range(n):
    if nums_copy[i] <= nums[i]/2:
        ans += 1

print(ans)
