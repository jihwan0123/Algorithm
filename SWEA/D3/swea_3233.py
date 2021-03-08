# 3233. 정삼각형 분할 놀이

import sys

sys.stdin = open('swea_3233.txt')

result = []

for tc in range(1, 1 + int(input())):
    a, b = map(int, input().split())
    c = int(a / b) ** 2
    result.append('#{} {}'.format(tc, c))

print('\n'.join(result))
