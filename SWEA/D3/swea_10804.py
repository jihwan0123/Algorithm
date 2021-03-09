# 10804. 문자열의 거울상

import sys

sys.stdin = open('swea_10804.txt')

for tc in range(1, 1 + int(input())):
    words = list(input())
    result = []
    for i in range(len(words) - 1, -1, -1):
        if words[i] == 'b':
            result.append('d')
        elif words[i] == 'p':
            result.append('q')
        elif words[i] == 'q':
            result.append('p')
        elif words[i] == 'd':
            result.append('b')

    print('#{} {}'.format(tc, ''.join(result)))
