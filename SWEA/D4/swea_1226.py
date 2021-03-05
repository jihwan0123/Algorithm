# 1226. 미로

import sys

sys.stdin = open('swea_1226.txt')

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def get_start_position(a, length):
    for i in range(length):
        for j in range(length):
            if a[i][j] == 2:
                return i, j
    return 'error'


def bfs_maze(cr, cc):
    queue = [(cr, cc)]
    maze[cr][cc] = 1
    while queue:
        nr, nc = queue.pop(0)
        for dr, dc in dxy:
            row = nr + dr
            col = nc + dc
            if row < 0 or row >= n or col < 0 or col >= n:
                continue
            elif maze[row][col] == 3:
                return 1
            elif not maze[row][col]:
                maze[row][col] = 1
                queue.append((row, col))
    return 0


for tc in range(1, 11):
    N = int(input())
    n = 16
    maze = [list(map(int, input())) for _ in range(n)]
    sr, sc = get_start_position(maze, n)
    result = bfs_maze(sr, sc)

    print('#{} {}'.format(tc, result))
