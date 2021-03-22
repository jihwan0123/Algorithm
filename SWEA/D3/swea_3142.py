# 3142. 영준이와 신비한 뿔의 숲

import sys

sys.stdin = open('swea_3142.txt')

for tc in range(1, 1 + int(input())):
    n, m = map(int, input().split())
    # n : 뿔, m : 짐승 수
    a = n - m
    # 트윈 혼
    b = m - a
    # 유니콘
    print('#{} {} {}'.format(tc, b, a))
