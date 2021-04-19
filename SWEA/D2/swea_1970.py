# 1970. 쉬운 거스름돈

import sys

sys.stdin = open('swea_1970.txt')

money = (50000, 10000, 5000, 1000, 500, 100, 50, 10)
for tc in range(1, 1 + int(input())):
    n = int(input())
    change = [0] * 8
    for idx, value in enumerate(money):
        if n >= value:
            cnt = n // value
            change[idx] += cnt
            n -= value * cnt

    print('#%d\n%s' % (tc, ' '.join(map(str, change))))
