# 5176. 이진탐색

import sys

sys.stdin = open('swea_5176.txt')


def create_tree(n):
    global cnt
    if n <= N:
        create_tree(n * 2)
        nodes[n] = cnt
        cnt += 1
        create_tree(n * 2 + 1)


for tc in range(1, 1 + int(input())):
    N = int(input())
    nodes = [0] * (N + 1)
    cnt = 1
    create_tree(1)
    print('#{} {} {}'.format(tc, nodes[1], nodes[N // 2]))
