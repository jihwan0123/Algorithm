# 1211. Ladder2

import sys

sys.stdin = open('swea_1211.txt')

dxy = [[0, -1], [1, 0], [-1, 0]]


def count_ladder(idx):
    row, col = 0, 0
    cnt = 0
    n = 100
    row = idx
    col = n - 1
    d = 0
    while col:
        dr, dc = dxy[d]
        row += dr
        col += dc
        cnt += 1
        if col == 0:
            return cnt, row
        if row == n - 1:
            if ladder[col][row - 1] and d == 0:
                d = 2
            else:
                d = 0

        elif row == 0:
            if ladder[col][row + 1] and d == 0:
                d = 1
            else:
                d = 0

        else:
            if d == 0:
                if ladder[col][row + 1]:
                    d = 1
                elif ladder[col][row - 1]:
                    d = 2

            elif d == 1:
                if ladder[col - 1][row]:
                    d = 0

            elif d == 2:
                if ladder[col - 1][row]:
                    d = 0


for tc in range(1, 11):
    a = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    count = 0
    result = []

    for i in ladder[-1]:
        if i:
            result.append(count_ladder(count))
        count += 1

    _min = float('inf')
    _idx = 0

    for i in result:
        if _min > i[0]:
            _min = i[0]
            _idx = i[1]
    print('#{} {}'.format(a, _idx))
