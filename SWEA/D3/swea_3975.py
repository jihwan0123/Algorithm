# 3975. 승률 비교하기

import sys

sys.stdin = open('swea_3975.txt')

res = []

for tc in range(1, 1 + int(input())):
    a, b, c, d = map(int, input().split())
    x = a / b
    y = c / d
    if x == y:
        result = 'DRAW'
    elif x > y:
        result = "ALICE"
    else:
        result = "BOB"
    res.append('#{} {}'.format(tc, result))

print('\n'.join(res))
