# 2814. 최장 경로

import sys

sys.stdin = open('swea_2814.txt')


def dfs(v, cnt):
    global ans
    ans = max(ans, cnt)

    for i in adj[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt + 1)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    ans = 0
    for _ in range(M):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    # 정점 1부터 N까지 존재
    for x in range(1, N + 1):
        visited[x] = 1
        dfs(x, 1)
        visited[x] = 0

    print('#%d %d' % (tc, ans))
