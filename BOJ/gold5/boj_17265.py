# 17265. 나의 인생에는 수학과 함께

import sys
input = sys.stdin.readline


def dfs(x, y, s, cnt):
    global minV, maxV
    if x == n-1 and y == n-1:
        minV = min(minV, int(s))
        maxV = max(maxV, int(s))
        return

    if y + 1 < n:
        if cnt % 2:
            dfs(x, y+1, str(s) + arr[x][y+1], cnt+1)
        else:
            dfs(x, y+1, eval(str(s) + arr[x][y+1]), cnt+1)

    if x + 1 < n:
        if cnt % 2:
            dfs(x+1, y, str(s) + arr[x+1][y], cnt+1)
        else:
            dfs(x+1, y, eval(str(s) + arr[x+1][y]), cnt+1)


n = int(input())
arr = [input().split() for _ in range(n)]
minV, maxV = 987654321, -987654321
dfs(0, 0, arr[0][0], 1)

print(maxV, minV)
