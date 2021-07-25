# 16973. 직사각형 탈출
import sys
from collections import deque
input = sys.stdin.readline

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

N, M = map(int, input().split())
# N * M 격자판의 크기
maps = [list(map(int, input().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())
visited = [[0] * M for _ in range(N)]
visited[Sr - 1][Sc - 1] = 1

walls = []
for i in range(N):
    for j in range(M):
        if maps[i][j]:
            walls.append((i, j))


def check(a, b):
    if a+H-1 >= N or b+W-1 >= M:  # 범위 벗어나면 False
        return False
    for x, y in walls:  # 범위 안에 벽이 있는지 체크
        if a <= x < a+H and b <= y < b+W:
            return False
    return True


def bfs():
    queue = deque([(Sr - 1, Sc - 1, 0)])
    while queue:
        x, y, cnt = queue.popleft()
        # 목적 좌표 도달하면 cnt
        if x == Fr - 1 and y == Fc - 1:
            return cnt

        # 시작 점 기준으로 4방향 탐색
        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y
            if nx < 0 or ny < 0 or nx + H > N or ny + W > M or visited[nx][ny]:
                continue
            if check(nx, ny):
                visited[nx][ny] = 1
                queue.append((nx, ny, cnt + 1))
    return -1


print(bfs())
