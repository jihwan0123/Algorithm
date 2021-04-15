# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

import sys

sys.stdin = open('swea_5201.txt', encoding='utf-8')

for tc in range(1, 1 + int(input())):
    n, m = map(int, input().split())
    # n : 컨테이너 수, m : 트럭 수
    # w = sorted((map(int, input().split())))
    w = sorted((map(int, input().split())), reverse=True)
    # 화물 무게
    # t = sorted((map(int, input().split())))
    t = sorted((map(int, input().split())), reverse=True)
    # 트럭 적재용량
    total = 0
    w_idx = t_idx = 0
    while w_idx < n and t_idx < m:
        x = w[w_idx]
        w_idx += 1
        if x <= t[t_idx]:
            total += x
            t_idx += 1

    # while w and t:
    #     x = w.pop()
    #     if x <= t[-1]:
    #         total += x
    #         t.pop()

    print('#%d %d' % (tc, total))
