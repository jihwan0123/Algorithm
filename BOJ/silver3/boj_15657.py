# 15657. N과 M (8)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int,input().split()))
nums.sort()

def dfs(lev, cur, num):
    if lev == m:
        print(' '.join(map(str, num)))
        return
    
    for i in range(cur, n):
        dfs(lev+1, i, num+[nums[i]])

dfs(0, 0, [])