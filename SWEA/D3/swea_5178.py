# 11759. 노드의 합

import sys

sys.stdin = open('swea_5178.txt')


def cal_sum(idx):
    if idx > N:
        return 0
    if tree[idx]:
        return tree[idx]
    return cal_sum(idx * 2) + cal_sum(idx * 2 + 1)


for tc in range(1, 1 + int(input())):
    N, M, L = map(int, input().split())
    # N : 노드의 개수
    # M : 리프 노드의 개수
    # 값을 출력할 노드 번호 L
    tree = [0] * (N + 1)
    for i in range(M):
        node, v = map(int, input().split())
        tree[node] = v
    # print(tree)

    print('#{} {}'.format(tc, cal_sum(L)))
