# 16973. 직사각형 탈출
import sys

sys.stdin = open('boj_16973.txt')

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

N, M = map(int, sys.stdin.readline().split())
# N * M 격자판의 크기
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, sys.stdin.readline().split())
queue = [(Sr - 1, Sc - 1, 0)]
visited = [[0] * M for _ in range(N)]
visited[Sr - 1][Sc - 1] = 1


def check(a, b):
    for i in range(a, a + H):
        for j in range(b, b + W):
            if maps[i][j]:
                return False
    return True


def bfs():
    while queue:
        x, y, cnt = queue.pop(0)
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
