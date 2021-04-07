# 11758. 이진 힙

import sys

sys.stdin = open('swea_5177.txt')


def create_tree(num):
    if num // 2:
        if tree[num] < tree[num // 2]:
            tree[num], tree[num // 2] = tree[num // 2], tree[num]
            create_tree(num // 2)


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    tree = [0]
    nodes = list(map(int, input().split()))
    for i in range(N):
        tree.append(nodes[i])
        create_tree(i + 1)
    res = 0

    while N:
        res += tree[N // 2]
        N = N // 2

    print('#{} {}'.format(tc, res))
