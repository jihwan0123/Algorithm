# 2667. 단지번호붙이기

n = int(input())

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def dfs(x, y):
    global cnt
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and houses[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            cnt += 1
            dfs(nx, ny)


houses = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if houses[i][j] and not visited[i][j]:
            cnt = 1
            visited[i][j] = 1
            dfs(i, j)
            res.append(cnt)

print(len(res))
for i in sorted(res):
    print(i)
