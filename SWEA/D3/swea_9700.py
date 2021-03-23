# 9700. USB 꽂기의 미스터리

import sys

sys.stdin = open('swea_9700.txt')

for tc in range(1, 1 + int(input())):
    p, q = map(float, input().split())

    s1 = (1 - p) * q
    s2 = p * (1 - q) * q
    if s1 > s2:
        res = 'NO'
    else:
        res = 'YES'
    print('#{} {}'.format(tc, res))
