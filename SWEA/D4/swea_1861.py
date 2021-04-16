# 1861. 정사각형 방

import sys

sys.stdin = open('swea_1861.txt')
'''
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
result = []
for tc in range(1, 1 + int(input())):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    n = N ** 2 + 1
    visited = [0] * n
    for x in range(N):
        for y in range(N):
            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if A[x][y] + 1 == A[nx][ny]:
                        visited[A[x][y]] = 1
    start = length = 1
    res = []
    for i in range(1, n):
        if visited[i]:
            length += 1
        else:
            res.append((start, length))
            length = 1
            start = i + 1

    res.sort(key=lambda k: (-k[1], k[0]))
    result.append('#%d %d %d' % (tc, res[0][0], res[0][1]))

print('\n'.join(result))
'''

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
result = []
for tc in range(1, 1 + int(input())):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    n = N ** 2 + 1
    visited = [0] * n
    for x in range(N):
        for y in range(N):
            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if A[x][y] + 1 == A[nx][ny]:
                        visited[A[x][y]] = 1
    start = length = 1
    res = []
    res1 = res2 = 0
    for i in range(1, n):
        if visited[i]:
            length += 1
        else:
            if length > res2:
                res2 = length
                res1 = start
            length = 1
            start = i + 1

    result.append('#%d %d %d' % (tc, res1, res2))

print('\n'.join(result))
