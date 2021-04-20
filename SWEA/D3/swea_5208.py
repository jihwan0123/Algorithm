# 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2

import sys

sys.stdin = open('swea_5208.txt')


def bus(level, cnt):
    global minV
    if cnt >= minV:
        return

    elif level + M[level] >= n:
        minV = cnt
        return

    for i in range(1, M[level] + 1):
        bus(level + i, cnt + 1)


for tc in range(1, 1 + int(input())):
    x = list(map(int, input().split()))
    N = x[0]  # 정류장 수
    M = x[1:] + [0]  # 정류장 별 배터리 용량
    n = len(M) - 1
    minV = 987654321
    bus(0, 0)
    print('#{} {}'.format(tc, minV))
