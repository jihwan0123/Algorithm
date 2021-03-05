# 10202. 문자열 동화

import sys

sys.stdin = open('swea_10202.txt')

T = int(input())

for tc in range(1, 1 + T):
    n = int(input())
    a = input()  # 길이가 n인 문자열 a,b,c
    b = input()
    c = input()

    counter = 0
    for i in range(n):
        if a[i] == b[i] == c[i]:
            continue
        else:
            same = {a[i], b[i], c[i]}  # 같은 만큼 남는다.
            if len(same) == 2:
                counter += 1
            else:
                counter += 2
    print('#{} {}'.format(tc, counter))
