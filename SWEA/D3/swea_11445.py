# 11445. 무한사전

import sys

sys.stdin = open('swea_11445.txt')

for tc in range(1, 1 + int(input())):
    P = input().strip()
    Q = input().strip()

    if P + 'a' == Q:
        result = 'N'
    else:
        result = 'Y'

    print('#{} {}'.format(tc, result))
