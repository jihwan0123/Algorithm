# 16236. 아기 상어

from collections import deque
import sys
input = sys.stdin.readline


def find_start():
    for i in range(n):
        for j in range(n):
            if fishes[i][j] == 9:
                fishes[i][j] = 0
                return (i, j)


def bfs(a, b):
    global shark
    q = deque([(a, b)])
    visited = [[0] * n for _ in range(n)]
    visited[a][b] = 1
    eatable = []
    while q:
        x, y = q.popleft()
        # 먹을 수 있는 물고기를 찾은 상태에서 더 먼 거리를 탐색하려고 하면 종료
        if eatable and visited[x][y] > eatable[0][0]:
            continue
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if fishes[nx][ny] == 0 or fishes[nx][ny] == shark:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                elif 0 < fishes[nx][ny] < shark:
                    # 먹을 수 있는 물고기 저장, 먹을 수 있는 물고기를 만나면 q에 넣지 않아도 된다.
                    eatable.append((visited[x][y], nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    if eatable:
        return sorted(eatable)[0]
    else:
        return (-1, -1, -1)


dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n = int(input())
fishes = [list(map(int, input().split())) for _ in range(n)]
shark = 2 # 초기 상어의 크기
x, y = find_start() # 아기상어 초기 위치 찾기
ans = eat_cnt = 0
while True:
    cnt, x, y = bfs(x, y)
    # print('x:', x, 'y:', y, 'cnt:', cnt)
    # 먹을 수 있는 물고기가 없으면 종료
    if cnt == -1:
        break
    if shark > fishes[x][y]:  # 먹을 수 있으면
        eat_cnt += 1  # 먹은 개수 추가
        fishes[x][y] = 0  # 빈칸으로 변경
    if eat_cnt >= shark:  # 아기상어 크기만큼 먹었으면 크기 +1
        shark += 1
        eat_cnt = 0
    ans += cnt # 이동 횟수 추가

print(ans)
