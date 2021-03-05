# 1219. 길찾기

import sys

sys.stdin = open('swea_1219.txt')


def DFS_AL(AL):
    visited = [0] * 100
    stack = [0]
    while stack:
        node = stack.pop()
        if node == 99:
            return 1
        if not visited[node]:
            visited[node] = 1
            for n in AL[node]:
                if not visited[n]:
                    stack.append(n)

    return 0


for tc in range(1, 11):
    t, V = map(int, input().split())
    line = list(map(int, input().split()))
    edges = [(line[i], line[i + 1]) for i in range(0, V * 2, 2)]

    AL = [[] for _ in range(100)]
    for s, e in edges:
        AL[s].append(e)

    print('#{} {}'.format(tc, DFS_AL(AL)))
