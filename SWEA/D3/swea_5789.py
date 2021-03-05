# 5789. 현주의 상자 바꾸기

import sys

sys.stdin = open('swea_5789.txt')

T = int(input())

for tc in range(1, 1 + T):
    n, q = map(int, input().split())
    result = [0] * n
    for a in range(1, q + 1):
        l, r = map(int, input().split())
        for i in range(l - 1, r):
            result[i] = a

    print('#%d' % tc, end=' ')
    print(*result)
