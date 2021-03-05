# 1209. Sum

import sys

sys.stdin = open('swea_1209.txt', encoding='utf-8')


def sum_list(args):
    total = 0
    for arg in args:
        total += arg

    return total


T = 10

for tc in range(1, 1 + T):
    a = int(input())
    input_list = [list(map(int, input().split())) for _ in range(100)]
    result = list(input_list)
    result1 = []
    result2 = []

    k = 0

    # 오른쪽 대각선
    for i in range(100):
        result1.append(input_list[i][i])

    # 왼쪽 대각선
    for i in range(99, -1, -1):
        # (99,0) (98,1) (97,2) ... (0, 99)
        result2.append(input_list[k][i])
        k += 1

    col_list = zip(*input_list)

    result.append(result1)
    result.append(result2)

    _max = 0

    for i in result:
        m = sum_list(i)
        if _max < m:
            _max = m

    for j in col_list:
        m = sum_list(j)
        if _max < m:
            _max = m

    print('#{} {}'.format(a, _max))
