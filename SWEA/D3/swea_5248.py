# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기

import sys

sys.stdin = open('swea_5248.txt')


# union find
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    edge = list(map(int, input().split()))
    adj = [[] for _ in range(N + 1)]
    p = list(range(N + 1))
    for i in range(M):
        n1 = edge[i * 2]
        n2 = edge[i * 2 + 1]
        # adj[n1].append(n2)
        # adj[n2].append(n1)
        union(n1, n2)
    cnt = 0
    # for i in range(1, N + 1):
    #     for j in adj[i]:
    #         union(i, j)
    for i in range(1, N + 1):
        if i == p[i]:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
