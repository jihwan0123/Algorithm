# 1865. 동철이의 일 분배

import sys

sys.stdin = open('swea_1865.txt')


def f(level, p):
    global maxP
    if p <= maxP:
        return

    if level >= N:
        maxP = max(maxP, p)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            f(level + 1, p * (P[level][i]))
            visited[i] = 0


res = []
for tc in range(1, 1 + int(input())):
    N = int(input())
    P = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]
    visited = [0] * N
    maxP = 0
    f(0, 1)
    res.append('#{} {:6f}'.format(tc, maxP * 100))

print('\n'.join(res))

'''
for tc in range(1, 1 + int(input())):
    n = int(input())
    p = [list(map(lambda x: x / 100, map(int, input().split()))) for _ in range(n)]

    d = [0] * (1 << n)
    d[0] = 1
    for mask in range(1 << n):
        x = sum(1 for i in range(n) if mask & (1 << i))
        for j in range(n):
            if mask & (1 << j) == 0:
                d[mask | (1 << j)] = max(d[mask | (1 << j)], d[mask] * p[x][j])

    print('#{} {:6f}'.format(tc, d[-1] * 100))
'''
