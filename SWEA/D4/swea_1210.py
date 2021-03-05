# 1210. Ladder1

import sys

sys.stdin = open('swea_1210.txt')

T = 10

dxy = [[0, -1], [1, 0], [-1, 0]]
# row, col
# 상 우 좌 순서

for tc in range(1, 1 + T):
    a = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # print(ladder[99][57])
    row, col, idx = 0, 0, 0

    for i in ladder[-1]:
        if i == 2:
            break
        else:
            idx += 1

    # 출발 좌표: (idx, 99)
    n = len(ladder)
    row = idx
    # print(idx)
    col = n - 1
    # 위쪽으로 출발
    d = 0
    # 0열까지 올라올때까지 반복
    while col:
        # 위쪽방향으로 시작
        dr, dc = dxy[d]
        row += dr
        col += dc
        # print(row, col)
        if col == 0:
            break
        # 제일 오른쪽일때 왼쪽만 검사
        if row == n - 1:
            if ladder[col][row - 1] and d == 0:
                d = 2
            else:
                d = 0

        # 제일 왼쪽일때 오른쪽만 검사
        elif row == 0:
            if ladder[col][row + 1] and d == 0:
                d = 1
            else:
                d = 0

        # 가운데 일때
        else:
            # 위로 가는중일때
            if d == 0:
                # 위로 가다가 오른쪽
                if ladder[col][row + 1]:
                    d = 1
                # 위로 가다가 왼쪽
                elif ladder[col][row - 1]:
                    d = 2


            # 오른쪽으로 가는중일때
            elif d == 1:
                # 오른쪽 가다가 위쪽
                if ladder[col - 1][row]:
                    d = 0

            # 왼쪽으로 가는중일때
            elif d == 2:
                # 왼쪽 가다가 위쪽
                if ladder[col - 1][row]:
                    d = 0

    print('#{} {}'.format(a, row))
