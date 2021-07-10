# 16234. 인구 이동

import sys
from collections import deque
input = sys.stdin.readline

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 국경선 공유


def bfs(a, b, c, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = c
    total = nations[a][b]
    cnt = 1
    chk = False
    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and (L <= abs(nations[x][y] - nations[nx][ny]) <= R):
                q.append((nx, ny))
                chk = True
                cnt += 1
                total += nations[nx][ny]
                visited[nx][ny] = c

    return total // cnt, chk


N, L, R = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]
ans = 0
visited = [[0] * N for _ in range(N)]
while True:
    x = 0
    populations = []
    visited = [[0] * N for _ in range(N)]
    nums = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and nations[i][j]:
                x += 1
                population, check = bfs(i, j, x, visited)  # 연합별로 구역 체크하기
                if check:
                    nums.append(x)
                    populations.append(population)

    # 이동하기
    if not populations:
        print(ans)
        break
    

    for ii in range(N):
        for jj in range(N):
            a = 0
            for kk in nums:
                if visited[ii][jj] == kk:
                    visited[ii][jj] = 0
                    nations[ii][jj] = populations[a]
                    a += 1
                    break
    print(nations)
    ans += 1
