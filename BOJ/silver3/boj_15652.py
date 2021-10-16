# 15652. N과 M (4)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(range(1, n+1))

def dfs(lev, cur, num):
    if lev == m:
        print(' '.join(map(str, num)))
        return
    
    for i in range(n):
        if i < cur: continue
        dfs(lev+1, i, num+[nums[i]])

dfs(0, 0, [])