# 17484. 진우의 달 여행(Small)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
fuels = [list(map(int, input().split())) for _ in range(n)]


def dfs(before, curSum, x, y):
    global minF
    if x == n-1:
        minF = min(minF, curSum)
        return

    for i in range(3):
        if i != before:
            nx, ny = x + dxy[i][0], y + dxy[i][1]
            if 0 <= nx < n and 0 <= ny < m and (curSum + fuels[nx][ny] < minF):
                dfs(i, curSum + fuels[nx][ny], nx, ny)

dxy = [(1, -1), (1, 0), (1, 1)]
minF = sys.maxsize

# 시작지점 (0, m) 에서 시작
for i in range(m):
    dfs(-1, fuels[0][i], 0, i)
print(minF)
