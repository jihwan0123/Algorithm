# 3143. 가장 빠른 문자열 타이핑

import sys

sys.stdin = open('swea_3143.txt')

for tc in range(1, 1 + int(input())):
    A, B = input().split()
    print('#{} {}'.format(tc, len(A.replace(B, 'x'))))
