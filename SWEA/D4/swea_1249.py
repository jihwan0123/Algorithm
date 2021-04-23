# 1249. [S/W 문제해결 응용] 4일차 - 보급로

import sys

sys.stdin = open('swea_1249.txt')

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs():
    D = [[float('inf')] * N for _ in range(N)]
    D[0][0] = 0
    queue = [(0, 0)]
    rp = 0
    while rp < len(queue):
        x, y = queue[rp]
        rp += 1
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                nD = D[x][y] + data[nx][ny]
                if D[nx][ny] > nD:
                    D[nx][ny] = nD
                    queue.append((nx, ny))

    return D[N - 1][N - 1]


for tc in range(1, 1 + int(input())):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    print('#{} {}'.format(tc, bfs()))
