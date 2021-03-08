# 3260. 두 수의 덧셈

import sys

sys.stdin = open('swea_3260.txt')

for tc in range(1, 1 + int(input())):
    a, b = map(int, input().split())
    print('#{} {}'.format(tc, a + b))
