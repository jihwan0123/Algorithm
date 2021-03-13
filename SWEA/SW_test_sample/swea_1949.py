# 1949. [모의 SW 역량테스트] 등산로 조성

import sys

sys.stdin = open('swea_1949.txt')

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def find_top():
    top = -1
    for i in range(n):
        for j in range(n):
            if top < mapping[i][j]:
                top = mapping[i][j]
                max_point.clear()
                max_point.append((i, j))
            elif top == mapping[i][j]:
                max_point.append((i, j))


def dfs(i, j, c, s):
    # i,j 진입한 칸의 좌표
    # c: 남은 깎음 횟수
    # s : 이전까지의 등산로 길이
    global result
    visited[i][j] = 1

    if s > result:
        result = s

    for dx, dy in dxy:
        row = i + dx
        col = j + dy
        if 0 <= row < n and 0 <= col < n and not visited[row][col]:
            if mapping[i][j] > mapping[row][col]:
                dfs(row, col, c, s + 1)

            elif c and mapping[i][j] > mapping[row][col] - c:
                d = abs(mapping[i][j] - mapping[row][col]) + 1
                mapping[row][col] -= d
                dfs(row, col, 0, s + 1)
                mapping[row][col] += d
            else:
                continue
        else:
            continue
    visited[i][j] = 0


for tc in range(1, 1 + int(input())):
    n, k = map(int, input().split())
    mapping = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    max_point = []
    find_top()
    result = 1
    for x, y in max_point:
        dfs(x, y, k, 1)

    print('#{} {}'.format(tc, result))

