# 1987. 알파벳 = 시간초과

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = 0
v = {}
v[arr[0][0]] = 1
visited = [[False] * c for _ in range(r)]
visited[0][0] = True


def dfs(x, y, cnt):
    global ans
    ans = max(cnt, ans)
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and not v.get(arr[nx][ny]):
            v[arr[nx][ny]] = 1
            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1)
            v[arr[nx][ny]] = 0
            visited[nx][ny] = False


dfs(0, 0, 1)
print(ans)