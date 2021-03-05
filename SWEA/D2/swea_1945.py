# 1945. 간단한 소인수분해

import sys

sys.stdin = open('fac_input.txt')

T = int(input())

for tc in range(1, 1 + T):
    num = int(input())
    result = [0] * 5
    while num:
        if num % 2 == 0:
            result[0] += 1
            num /= 2

        elif num % 3 == 0:
            result[1] += 1
            num /= 3

        elif num % 5 == 0:
            result[2] += 1
            num /= 5

        elif num % 7 == 0:
            result[3] += 1
            num /= 7

        elif num % 11 == 0:
            result[4] += 1
            num /= 11
        else:
            break
    print('#%d' % tc, end=' ')
    print(*result)
