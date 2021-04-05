# 1231. 중위순회

import sys

sys.stdin = open('swea_1231.txt')


def inorder(n):
    n = int(n)
    if n > 0:
        # left
        inorder(left[n])
        # 가운데
        res.append(tree[n - 1][1])
        # right
        inorder(right[n])


for tc in range(1, 11):
    N = int(input())
    # 루트 정점 번호 = 1
    tree = [list(input().split()) for _ in range(N)]
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for i in range(0, N):
        if len(tree[i]) == 4:
            left[i + 1] = int(tree[i][2])
            right[i + 1] = int(tree[i][3])

        elif len(tree[i]) == 3:
            left[i + 1] = int(tree[i][2])
    res = []
    root = 1
    inorder(root)
    print('#%d ' % tc, end='')
    print(''.join(res))
