# 1012. 유기농 배추

from collections import deque
import sys
input = sys.stdin.readline

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(a, b, arr):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = 0


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    arr = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                bfs(i, j, arr)
                cnt += 1
    print(cnt)
