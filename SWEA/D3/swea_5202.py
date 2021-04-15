# 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크

import sys

sys.stdin = open('swea_5202.txt')

for tc in range(1, 1 + int(input())):
    n = int(input())
    times = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])
    cur = cnt = 0
    for s, e in times:
        if cur <= s:
            cnt += 1
            cur = e

    print('#%d %d' % (tc, cnt))
