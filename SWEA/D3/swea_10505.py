# 10505. 소득 불균형

import sys

sys.stdin = open('swea_10505.txt')

for tc in range(1, 1 + int(input())):
    N = int(input())
    income = list(map(int, input().split()))
    average = sum(income) / N
    cnt = 0
    for i in income:
        if i <= average:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
