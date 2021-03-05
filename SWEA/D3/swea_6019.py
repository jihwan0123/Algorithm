# 6019. 기차 사이의 파리

import sys

sys.stdin = open('swea_6019.txt')

for tc in range(1, 1 + int(input())):
    D, A, B, F = map(int, input().split())
    # D : 기차 사이의 거리
    # A : 기차 A의 속력
    # B : 기차 B의 속력
    # F: 파리의 속력

    C = A + B
    result = F * D / C
    # 시간 = 거리/속력
    print('#%d %f' % (tc, result))
