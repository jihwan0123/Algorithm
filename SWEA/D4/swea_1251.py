# 1251. [S/W 문제해결 응용] 4일차 - 하나로

import sys

sys.stdin = open('swea_1251.txt')


def find_charges(x1, x2, y1, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) * E


def extract_min(visit, distance):
    min_key = float('inf')
    min_idx = 0
    for i in range(N):
        if not visit[i] and distance[i] < min_key:
            min_idx = i
            min_key = distance[i]
    return min_idx


def prim(s):
    key = [float('inf')] * N
    key[s] = 0
    mst = [0] * N
    for _ in range(N):
        u = extract_min(mst, key)
        mst[u] = 1

        for v in range(N):
            if not mst[v]:
                key[v] = min(key[v], adj[u][v])

    return sum(key[1:])


for tc in range(1, 1 + int(input())):
    N = int(input())  # N : 섬의 개수
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    # adj[i][j] : i와 j 사이의 가중치
    adj = [[0] * N for _ in range(N)]
    E = float(input())  # E : 세율 실수
    # 환경부담금: 환경부담세율(E) * (해저터널 길이(L) **2)
    for i in range(N):
        for j in range(N):
            adj[i][j] = find_charges(x[i], x[j], y[i], y[j])

    print('#%d' % tc, round(prim(0)))

'''
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def Kruskal(N, edge):
    p = [i for i in range(N + 1)]  # 대표원소 초기화
    L2 = cnt = 0
    for w, u, v in edge:
        if find_set(u) != find_set(v):
            p[find_set(v)] = find_set(u)
            cnt += 1
            L2 += w
            if cnt == N - 1:
                return L2


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    # 완전 그래프 정리
    adj = [[0] * N for _ in range(N)]  # 인접 행렬
    for i in range(N):
        for j in range(N):
            adj[i][j] = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
            adj[j][i] = adj[i][j]

    edges = []  # 간선 정보 기준 저장
    for i in range(N):
        for j in range(i + 1, N):
            edges.append(((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2, i, j))
    edges.sort()
    print(Kruskal(0, edges))
'''
