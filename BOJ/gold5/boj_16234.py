# 16234. 인구 이동

import sys
from collections import deque
input = sys.stdin.readline

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 국경선 BFS로 체크
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

    if not chk:
        visited[a][b] = 0

    return total // cnt, chk


N, L, R = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]
ans = 0
visited = [[0] * N for _ in range(N)]
while True:
    x = 1
    populations = []
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                population, check = bfs(i, j, x, visited)  # 연합별로 구역 번호 체크
                # 연합이 생겼으면 추가 인구수 계산값 추가
                if check:
                    x += 1
                    populations.append(population)

    if not populations:
        print(ans)
        break

    # 이동하기
    for ii in range(N):
        for jj in range(N):
            for kk in range(1, x):
                if visited[ii][jj] == kk:
                    nations[ii][jj] = populations[kk-1]
                    break

    ans += 1


''' 처음 코드
# 16234. 인구 이동

import sys
from collections import deque
input = sys.stdin.readline

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 국경선 공유
def bfs(a, b, c, visited):
    q = deque()
    q.append((a,b))
    # q = [(a, b)]
    while q:
        # x, y = q.pop(0)
        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(nations[x][y] - nations[nx][ny]) <= R:
                q.append((nx, ny))
                visited[nx][ny] = c


def visited_clear():
    for i in range(N):
        for j in range(N):
            visited[i][j] = 0


N, L, R = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]
ans = 0
visited = [[0] * N for _ in range(N)]
while True:
    x = 0
    check = False
    visited_clear()
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and nations[i][j]:
                x += 1
                bfs(i, j, x, visited)  # 연합별로 구역 체크하기

    # 이동하기
    total = [0] * (x+1)
    cnt = [0] * (x+1)
    population = [0] * (x+1)
    nums = list(range(1, x+1))

    for i in range(N):
        for j in range(N):
            for n in nums:
                if visited[i][j] == n:
                    total[n] += nations[i][j]
                    cnt[n] += 1

    check = True
    for k in range(1, x+1):
        if cnt[k]:
            check = False
            population[k] = total[k] // cnt[k]

    if check:
        print(ans)
        break

    for ii in range(N):
        for jj in range(N):
            for n in nums:
                if visited[ii][jj] == n:
                    nations[ii][jj] = population[n]

    ans += 1
'''