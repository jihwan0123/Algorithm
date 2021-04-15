# 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합

import sys

sys.stdin = open('swea_5188.txt')

dxy = [[1, 0], [0, 1]]


def bfs():
    queue = [(0, 0)]
    visited = [[999] * N for _ in range(N)]
    visited[0][0] = data[0][0]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + data[nx][ny]
                    queue.append((nx, ny))

                elif visited[nx][ny] > visited[x][y] + data[nx][ny]:
                    visited[nx][ny] = visited[x][y] + data[nx][ny]
                    queue.append((nx, ny))

    return visited[N - 1][N - 1]


for tc in range(1, 1 + int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print('#%d %d' % (tc, bfs()))
