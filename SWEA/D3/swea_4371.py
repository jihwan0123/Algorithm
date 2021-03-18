# 4371. 항구에 들어오는 배

import sys

sys.stdin = open('swea_4371.txt')

for tc in range(1, 1 + int(input())):
    N = int(input())
    # N : 즐거운 날의 수
    happy_day = [int(input()) for i in range(N)]
    period = set()
    for i in range(1, len(happy_day)):
        check = True
        if period:
            for j in period:
                if (happy_day[i] - 1) % j == 0:
                    check = False
                    break
        if check:
            period.add(happy_day[i] - 1)

    print('#{} {}'.format(tc, len(period)))
