# 1974. 스도쿠 검증

import sys

sys.stdin = open('swea_1974.txt')


def is_sudoku(rows):
    nums = [0 for _ in range(10)]
    for r in rows:
        nums[r - 1] += 1
        if nums[r - 1] > 1:
            return False
    else:
        return True


for tc in range(1, 1 + int(input())):
    test = 1

    data = [list(map(int, input().split())) for _ in range(9)]

    for row in data:
        if not is_sudoku(row):
            test = 0
            break

    if not test:
        print('#{} {}'.format(tc, test))
        continue

    cols = list(zip(*data))

    for col in cols:
        if not is_sudoku(col):
            test = 0
            break

    if not test:
        print('#{} {}'.format(tc, test))
        continue

    for i in range(0, 9, 3):
        if not is_sudoku([data[a][b] for a in range(i, i + 3) for b in range(i, i + 3)]):
            test = 0
            break

    print('#{} {}'.format(tc, test))
