# 10726. 이진수 표현

import sys

sys.stdin = open('swea_10726.txt')

res = []

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())

    result = 'ON'

    for i in range(N):
        if M % 2:
            M = M // 2
        else:
            result = 'OFF'
            break

    res.append('#{} {}'.format(tc, result))

print('\n'.join(res))
