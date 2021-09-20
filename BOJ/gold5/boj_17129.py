# 17129. 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유

from collections import deque
import sys
input = sys.stdin.readline

dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]
n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]


def find_start(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '2':
                return i, j


def bfs(x, y):
    q = deque([(x, y)])
    visited = [[0] * m for _ in range(n)]
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != '1' and not visited[nx][ny]:
                if arr[nx][ny] == '3' or arr[nx][ny] == '4' or arr[nx][ny] == '5':
                    return visited[x][y] + 1
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


start_x, start_y = find_start(arr)
ans = bfs(start_x, start_y)
if ans:
    print('TAK')
    print(ans)
else:
    print('NIE')
