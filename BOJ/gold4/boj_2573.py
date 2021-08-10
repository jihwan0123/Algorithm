# 2573. 빙산

import sys
from collections import deque
input = sys.stdin.readline

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_iceberg():  # 현재 빙산이 있는 좌표 저장
    ice_exists = []
    for i in range(n):
        for j in range(m):
            if iceberg[i][j]:
                ice_exists.append((i, j))
    return ice_exists


def melt(ices):
    actions = []
    for ice in ices:
        cnt = 0
        for dx, dy in dxy:
            nx = ice[0] + dx
            ny = ice[1] + dy
            if 0 <= nx < n and 0 <= ny < m and iceberg[nx][ny] == 0:
                cnt += 1
        actions.append((ice[0], ice[1], cnt))

    for action in actions:
        if iceberg[action[0]][action[1]] - action[2] < 0:
            iceberg[action[0]][action[1]] = 0
        else:
            iceberg[action[0]][action[1]] -= action[2]


def bfs(s):  # 얼음 몇덩어리인지 확인
    a, b = s
    visited[a][b] = 1
    q = deque([s])
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and iceberg[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx, ny))

    return 1


n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]
ans = 0
while True:
    ans += 1
    before_ices = find_iceberg()  # 빙산이 남아 있는 좌표들 저장
    melt(before_ices)  # 빙산 녹는다
    after_ices = find_iceberg()  # 녹고 난 이후의 빙산의 좌표
    if len(after_ices) == 0:
        print(0)
        break
    visited = [[0] * m for _ in range(n)]
    check = 0
    # 빙산 몇덩어리로 나누어지는지 체크
    for after in after_ices:
        if not visited[after[0]][after[1]]:  # 방문 안했으면 bfs
            check += bfs(after)  # bfs 했으면 1씩 카운트
        if check > 1:
            break

    if check >= 2:
        print(ans)
        break
