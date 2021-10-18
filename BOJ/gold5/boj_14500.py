# 14500. 테트로미노

''' # 가지치기 전 = Python3 7760ms
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


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = False


for i in range(n):
    for j in range(m):
        x = []
        for dx, dy in dxy:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m:
                x.append(arr[nx][ny])
        if len(x) == 4:
            ans = max(ans, arr[i][j] + sum(x)-min(x))
        elif len(x) == 3:
            ans = max(ans, arr[i][j] + sum(x))

print(ans)
'''

# 가지치기 추가 Python3 280ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[False] * m for _ in range(n)]
maxV = max(map(max, arr))


def dfs(x, y, lev, total):
    global ans
    # 나머지 칸이 모두 최댓값이어도 안되는 경우 가지치기
    if total + (4 - lev) * maxV <= ans:
        return

    if lev == 4:
        ans = max(ans, total)
        return

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            # 한 칸 이동한 후에 원래 위치로 이동하면, 마지막 모양 체크 가능
            if lev == 2:
                visited[nx][ny] = True
                dfs(x, y, lev+1, total + arr[nx][ny])
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, lev+1, total + arr[nx][ny])
            visited[nx][ny] = False


# 4개 연속으로 되는 부분 체크
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = False

print(ans)
