# 7465. 창용마을 무리의 개수

import sys

sys.stdin = open('swea_7465.txt')


# union_find
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    p = list(range(N + 1))
    adj = [[] for _ in range(N + 1)]
    for i in range(M):
        n1, n2 = map(int, input().split())
        union(n1, n2)
    cnt = 0
    for i in range(1, N + 1):
        if i == p[i]:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
