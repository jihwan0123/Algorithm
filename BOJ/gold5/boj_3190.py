# 3190. 뱀

import sys
from collections import deque
input = sys.stdin.readline

dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N = int(input())
K = int(input())
boards = [[0]*N for _ in range(N)]
visited = [[0]*N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    boards[a-1][b-1] = 1

L = int(input())
directions = [input().split() for _ in range(L)]
x = y = 0
idx = 0
body = deque([(0, 0)])
visited[0][0] = 1
chk = False
ans = 0
for i in range(L):
    num = int(directions[i][0]) - ans
    while num:
        x += dxy[idx][0]
        y += dxy[idx][1]
        # 벽이나 자기자신 몸에 안부딪히면
        if 0 <= x < N and 0 <= y < N and not visited[x][y]:
            if boards[x][y]:  # 사과가 있으면 이동만
                boards[x][y] = 0
            else:  # 사과가 없으면 이동하고 꼬리 제거
                a, b = body.popleft()
                visited[a][b] = 0
            body.append((x, y))
            visited[x][y] = 1
        else:
            ans += 1
            chk = True
            break
        ans += 1
        num -= 1
    # 벽 부딪혔으면 종료
    if chk:
        break
    # 회전
    if directions[i][1] == 'L':
        idx -= 1
        if idx < 0:
            idx = 3
    else:
        idx += 1
        if idx > 3:
            idx = 0

# 명령이 끝났어도 안부딪혔으면
while not chk:
    # 마지막 방향으로 계속 이동하면서 체크
    x += dxy[idx][0]
    y += dxy[idx][1]
    if 0 <= x < N and 0 <= y < N and not visited[x][y]:
        ans += 1
    # 부딪히면 종료
    else:
        ans += 1
        chk = True
        break
print(ans)
