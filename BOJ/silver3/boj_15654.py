# 15654. N과 M (5)

from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = list(permutations(nums, m))
for a in ans:
    print(*a)