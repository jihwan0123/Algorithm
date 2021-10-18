# 14500. 테트로미노

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[False] * m for _ in range(n)]


def dfs(x, y, lev, total):
    global ans
    if lev == 4:
        ans = max(ans, total)
        return
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, lev+1, total + arr[nx][ny])
                visited[nx][ny] = False


# 4개 연속으로 되는 부분 체크
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = False

# 마지막 모양 체크
for i in range(n):
    for j in range(m):
        x = []
        for dx, dy in dxy:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m:
                x.append(arr[nx][ny])

        if len(x) == 4:  # 연결 가능한곳이 4개면
            ans = max(ans, arr[i][j] + sum(x)-min(x))  # 다 더한 후 최솟값을 뺀다.
        elif len(x) == 3:  # 연결 가능한곳이 3개면
            ans = max(ans, arr[i][j] + sum(x))  # 다 더한다.

print(ans)