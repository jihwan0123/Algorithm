# 5174. Tree 8일차 subtree

import sys

sys.stdin = open('swea_5174.txt')


def countNode(n):
    global cnt
    cnt += 1
    if AL.get(n):
        for i in AL.get(n):
            countNode(i)
    else:
        return


for tc in range(1, 1 + int(input())):
    E, N = map(int, input().split())
    # E : 간선의 개수, N : 노드
    nodes = list(map(int, input().split()))
    AL = {}
    for i in range(len(nodes) // 2):
        if AL.get(nodes[2 * i]):
            AL[nodes[2 * i]].append(nodes[2 * i + 1])
        else:
            AL[nodes[2 * i]] = [nodes[2 * i + 1]]

    cnt = 0
    countNode(N)
    print('#{} {}'.format(tc, cnt))
