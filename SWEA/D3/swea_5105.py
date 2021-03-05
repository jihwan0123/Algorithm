# 11629. 미로의 거리

import sys

sys.stdin = open('swea_11629.txt')

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def get_start_position(a, n):
    for i in range(n):
        for j in range(n):
            if a[i][j] == 2:
                return i, j
    return 'error'


def bfs_maze(cr, cc, level):
    queue = [(cr, cc)]
    visit[cr][cc] = level
    while queue:
        nr, nc = queue.pop(0)
        level = visit[nr][nc]
        for dr, dc in dxy:
            row = nr + dr
            col = nc + dc
            if row < 0 or row >= N or col < 0 or col >= N:
                continue
            elif maze[row][col] == 3:
                return level - 1
            elif not maze[row][col] and not visit[row][col]:
                visit[row][col] = level + 1
                queue.append((row, col))
    return 0


for tc in range(1, 1 + int(input())):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]

    sr, sc = get_start_position(maze, N)
    result = bfs_maze(sr, sc, 1)

    print('#{} {}'.format(tc, result))
