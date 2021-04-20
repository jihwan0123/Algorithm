# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용

import sys

sys.stdin = open('swea_5209.txt')


def f(level, total):
    global minV
    if total >= minV:
        return
    if level >= N:
        minV = min(minV, total)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            f(level + 1, total + V[level][i])
            visited[i] = 0


for tc in range(1, 1 + int(input())):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    minV = 987654321
    f(0, 0)
    print('#{} {}'.format(tc, minV))
