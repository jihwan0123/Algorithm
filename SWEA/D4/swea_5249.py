# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리

import sys

sys.stdin = open('swea_5249.txt')


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


for tc in range(1, 1 + int(input())):
    V, E = map(int, input().split())
    p = list(range(V + 1))
    graph = sorted([list(map(int, input().split())) for x in range(E)], key=lambda x: x[2])
    res = 0
    for n1, n2, w in graph:
        if find_set(n1) != find_set(n2):
            res += w
            union(n1, n2)
    print('#{} {}'.format(tc, res))
