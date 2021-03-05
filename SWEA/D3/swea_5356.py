# 5356. 의석이의 세로로 말해요

import sys

sys.stdin = open('swea_5356.txt')

T = int(input())

for tc in range(1, 1 + T):
    words = [input() for _ in range(5)]
    n = len(words[0])
    for i in words:
        if len(i) > n:
            n = len(i)

    for j in range(len(words)):
        a = len(words[j])
        while a != n:
            words[j] = words[j] + '*'
            a += 1

    result = []
    for i in range(n):
        for j in range(5):
            result.append(words[j][i])

    res = ''.join(result).replace('*', '')
    print('#{} {}'.format(tc, res))
