# 2468. 안전 영역

import sys
from collections import deque
input = sys.stdin.readline


dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(x, y, visited, height):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and regions[nx][ny] > height:
                visited[nx][ny] = True
                q.append((nx, ny))


def find(x):
    global ans
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if regions[i][j] > x and not visited[i][j]:
                cnt += 1
                bfs(i, j, visited, x)

    ans = max(ans, cnt)


n = int(input())
regions = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(101):
    find(i)

print(ans)

