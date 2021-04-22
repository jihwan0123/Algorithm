# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리

import sys

sys.stdin = open('swea_5251.txt')


def dijkstra(s):
    D = [float('inf')] * (N + 1)
    U = {s: 1}
    for a, b in adj[s]:
        D[b] = a
    D[0] = 0

    queue = [s]
    # while queue:
    #     x = queue.pop(0)
    for i in range(N):
        minV = float('inf')
        # 방문하지 않은 정점 중에 D 값이 가장 작은 정점 w 찾기
        for idx, value in enumerate(D):
            if U.get(idx):
                continue
            if minV > value:
                minV = value
                w = idx
                continue
        # 방문표시
        U[w] = 1
        # 최단거리 배열 갱신
        for ww, ee in adj[w]:
            if D[ee] > D[w] + ww:
                D[ee] = D[w] + ww
                # queue.append(ee)

    return D[N]


for tc in range(1, 1 + int(input())):
    N, E = map(int, input().split())
    # N : 연결지점 번호, E : 도로의 갯수
    adj = [[] for _ in range(N + 1)]
    # s, e, w 시작 끝 구간거리
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((w, e))
    # for i in adj:
    #     i.sort()
    # 가중치 기준으로 정렬
    print('#{} {}'.format(tc, dijkstra(0)))
