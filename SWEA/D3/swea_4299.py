# 4299. 태혁이의 사랑은 타이밍

import sys

sys.stdin = open('swea_4299.txt')

total_init = 11 * 1440 + 11 * 60 + 11

for tc in range(1, 1 + int(input())):
    D, H, M = map(int, input().split())
    ans = D * 1440 + H * 60 + M
    ans -= total_init
    if ans < 0:
        res = -1
    else:
        res = ans

    print('#{} {}'.format(tc, res))
