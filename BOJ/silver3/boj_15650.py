# 15650. N과 M (2)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(range(1, n+1))

def dfs(lev, cur, num):
    if lev == m:
        print(' '.join(map(str, num)))
        return
    
    for i in range(cur+1, n):
        dfs(lev+1, i, num+[nums[i]])

dfs(0, -1, [])