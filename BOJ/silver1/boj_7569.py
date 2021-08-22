# 7569. 토마토

import sys
from collections import deque
input = sys.stdin.readline

dxyz = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0),
        (1, 0, 0), (-1, 0, 0)]  # 4방향 + 위, 아래


m, n, h = map(int, input().split())
tomatos = [[list(map(int, input().split())) for _ in range(n)]
            for _ in range(h)]

# 익은 토마토 좌표 저장
ripe_tomatos = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatos[i][j][k] == 1:
                ripe_tomatos.append((i, j, k))

ans = 0
temp = [] # 임시저장용
while ripe_tomatos:
    z, x, y = ripe_tomatos.popleft()
    for dz, dx, dy in dxyz: # 6방향 돌면서 확인
        nz = z + dz
        nx = x + dx
        ny = y + dy
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and tomatos[nz][nx][ny] == 0: # 토마토가 안익었으면
            tomatos[nz][nx][ny] = 1 # 1로 변경 후
            temp.append((nz, nx, ny)) # 좌표 저장

    # deque에서 전부 꺼냈는데, 임시 저장한 좌표가 있으면
    if not ripe_tomatos and temp:
        # 토마토에 임시저장했던 좌표 넣어주고
        ripe_tomatos.extend(temp)
        # temp 초기화
        temp.clear()
        # 까지의 과정이 1 Day
        ans += 1

# 0이 남아있는지 확인
for tomato in tomatos:
    for t in tomato:
        if 0 in t: # 안익은게 있으면
            # -1 출력하고 종료
            print(-1)
            sys.exit()
# 다 익었으면 ans 출력
print(ans)
