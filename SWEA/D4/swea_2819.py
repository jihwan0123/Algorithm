# 2819. 격자판의 숫자 이어 붙이기

import sys

sys.stdin = open('swea_2819.txt')

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def dfs(n, x, y, num):
    if n == 7:
        res.add(num)
        return

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(n + 1, nx, ny, num + board[nx][ny])


for tc in range(1, 1 + int(input())):
    board = [input().split() for _ in range(4)]
    res = set()
    for i in range(4):
        for j in range(4):
            dfs(1, i, j, board[i][j])

    print('#{} {}'.format(tc, len(res)))
