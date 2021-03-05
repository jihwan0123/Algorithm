# 3499. 퍼펙트 셔플

import sys

sys.stdin = open('swea_3499.txt')

for tc in range(1, 1 + int(input())):
    N = int(input())
    cards = input().split()
    result = []

    # 홀수면
    if N % 2:
        # 앞에 + 1장
        n = N // 2 + 1
        for i in range(n):
            result.append(cards[i])
            if i != n - 1:
                result.append(cards[i + n])
    else:
        n = N // 2
        for i in range(n):
            result.append(cards[i])
            result.append(cards[i + n])

    # for i in range(n):
    #     result.append(cards[i])
    #     if i == n - 1 and N % 2:
    #         break
    #     result.append(cards[i+n])

    print('#{} {}'.format(tc, ' '.join(result)))
