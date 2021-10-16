# 15663. N과 M (9)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
ans = set()
used = [0] * (n+1)


def dfs(lev, num):
    if lev == m:
        ans.add(tuple(num))
        return

    for i in range(n):
        if used[i]:
            continue
        used[i] = 1
        dfs(lev+1, num+[nums[i]])
        used[i] = 0


dfs(0, [])

for a in sorted(ans):
    print(' '.join(map(str, a)))
