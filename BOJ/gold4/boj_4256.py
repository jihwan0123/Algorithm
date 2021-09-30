# 4256. 트리

import sys
input = sys.stdin.readline


def dfs(root, l, r):
    if l > r:
        return

    idx = index_list[preorder[root]]  # root index
    dfs(root+1, l, idx-1)  # 왼쪽
    dfs(root+(idx-l+1), idx+1, r)  # 오른쪽
    ans.append(preorder[root])  # 왼쪽 오른쪽 모두 종료했으면 오른쪽부터 저장


for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    # index 미리 저장
    index_list = [0] * (n+1)
    for i in range(n):
        index_list[inorder[i]] = i

    ans = []
    dfs(0, 0, n-1)
    print(*ans)
