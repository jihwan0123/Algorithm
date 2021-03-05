# 2805. 농작물 수확하기

import sys

sys.stdin = open('swea_2805.txt')

for tc in range(1, 1 + int(input())):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]

    total = 0
    r, c = n // 2, n // 2
    dr = 0
    i = 0

    while dr <= n // 2:
        for j in range(-n // 2 + i + 1, n // 2 - i + 1):
            if dr == 0:
                total += farm[r][c + j]
            else:
                total += farm[r + dr][c + j]
                total += farm[r - dr][c + j]
        dr += 1
        i += 1

    print('#{} {}'.format(tc, total))
