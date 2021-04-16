# 1486. 장훈이의 높은 선반

import sys

sys.stdin = open('swea_1486.txt')

'''
def f(i, s, rs):
    global minV
    if minV < s or s + rs < B:
        return

    if i == N:
        if s >= B:
            minV = min(minV, s)
        return

    f(i + 1, s + H[i], rs - H[i])
    f(i + 1, s, rs - H[i])


for tc in range(1, 1 + int(input())):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    minV = 10000 * 21
    f(0, 0, sum(H))
    print('#{} {}'.format(tc, minV - B))
'''

'''
def f(i, s):
    global minV
    if minV < s or minV == B:
        return

    if i == N:
        if s >= B:
            minV = min(minV, s)
        return
    if s + rs[i] < B:
        return
    f(i + 1, s + H[i])
    f(i + 1, s)


for tc in range(1, 1 + int(input())):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    minV = 200001
    rs = H.copy()
    for i in range(N - 2, -1, -1):
        rs[i] += rs[i + 1]

    f(0, 0)
    print('#{} {}'.format(tc, minV - B))
'''


def f(i, s):
    global minV
    if minV < s:
        return 0
    if minV == B:
        return 1

    if i == N:
        if s >= B:
            minV = min(minV, s)
        return 0

    if s + rs[i] < B:
        return 0

    if f(i + 1, s + H[i]):
        return 1
    if f(i + 1, s):
        return 1
    return 0


for tc in range(1, 1 + int(input())):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    minV = 200001
    rs = H.copy()
    for i in range(N - 2, -1, -1):
        rs[i] += rs[i + 1]

    f(0, 0)
    print('#{} {}'.format(tc, minV - B))
