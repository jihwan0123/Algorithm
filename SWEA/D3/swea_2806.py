# 2806. N-Queen

import sys


# sys.stdin = open('swea_2806.txt')


def bfs(n, level):
    global result
    if level == n:
        result += 1
        return

    for x in range(n):
        # col: 같은 열, diag1 : '\' 방향, diag2 : '/' 방향
        if x in col or (x + level) in diag1 or (x - level) in diag2:
            continue

        col.append(x)
        diag1.append(x + level)
        diag2.append(x - level)

        # 재귀로 다음 열,대각선 검사하면서 추가
        bfs(n, level + 1)

        col.remove(x)
        diag1.remove(x + level)
        diag2.remove(x - level)


for tc in range(1, 1 + int(input())):
    N = int(input())
    col, diag1, diag2 = [], [], []
    result = 0
    bfs(N, 0)

    print('#{} {}'.format(tc, result))
