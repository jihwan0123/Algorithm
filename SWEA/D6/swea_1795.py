# 1795. 인수의 생일 파티

import sys

sys.stdin = open('swea_1795.txt')


def dijkstra(s, adj, d):
    U = {s: 1}
    for i in range(N + 1):
        d[i] = adj[s][i]

    for _ in range(N):
        minV = 10000001
        # 방문하지 않은 정점 중에 D 값이 가장 작은 정점 w 찾기
        for idx, value in enumerate(d):
            if not U.get(idx) and minV > value:
                minV = value
                min_idx = idx
                continue
        # 방문표시
        U[min_idx] = 1
        # 최단거리 배열 갱신
        for j in range(1, N + 1):
            if min_idx != j and adj[min_idx][j] < 10000001:
                d[j] = min(d[j], d[min_idx] + adj[min_idx][j])


for tc in range(1, 1 + int(input())):
    N, M, X = map(int, input().split())
    adj1 = [[10000001] * (N + 1) for _ in range(N + 1)]  # 갈 때
    adj2 = [[10000001] * (N + 1) for _ in range(N + 1)]  # 올 때

    for _ in range(M):
        u, v, w = map(int, input().split())
        adj1[u][v] = w
        adj2[v][u] = w
    for i in range(N + 1):
        adj1[i][i] = 0
        adj2[i][i] = 0

    dist1 = [10000001] * (N + 1)
    dist2 = [10000001] * (N + 1)

    dijkstra(X, adj1, dist1)
    dijkstra(X, adj2, dist2)

    maxV = 0
    for k in range(1, N + 1):
        maxV = max(dist1[k] + dist2[k], maxV)

    print('#{} {}'.format(tc, maxV))
