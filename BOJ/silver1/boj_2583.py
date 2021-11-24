# 2583. 영역 구하기

import sys
from collections import deque
input = sys.stdin.readline

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for a in range(x1, x2):
        for b in range(y1, y2):
            arr[b][a] += 1


def bfs(x, y):
    q = deque([(x, y)])
    arr[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))
                cnt += 1
    return cnt


cnt = 0
res = []
for i in range(n):
    for j in range(m):
        if not arr[j][i]:
            res.append(bfs(j, i))
            cnt += 1

print(cnt)
print(*sorted(res))
