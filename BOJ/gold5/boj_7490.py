# 7490. 0 만들기

import sys
input = sys.stdin.readline


def dfs(lev):
    if lev == n-1:
        if eval(''.join(map(str, nums))) == 0:
            # 1-2 3-4 5+6 7 와 같이 공백 넣기
            res = nums.copy()
            for i in range(len(res)-1):
                if res[i].isdigit():
                    res[i] += ' '
            ans.append(''.join(map(str, res)))
        return

    temp = str(nums[lev])
    # +, -, '' 넣어본다.
    nums[lev] = temp + '+'
    dfs(lev+1)
    nums[lev] = temp + '-'
    dfs(lev+1)
    nums[lev] = temp
    dfs(lev+1)


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(range(1, n+1))
    ans = []
    dfs(0)
    print('\n'.join(sorted(ans)))
    print()
