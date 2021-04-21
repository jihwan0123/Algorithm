# 11942. 그래프에 Dijkstra 적용

import sys

sys.stdin = open('swea_11942.txt')


def dijkstra(s):
    # s : 시작 값
    # U: 방문표시
    U = {s: 1}
    # D : 가중치의 최솟값
    D = {x: float('inf') for x in graph}
    D[s] = 0
    for i in graph.get(s):
        D[i] = graph.get(s).get(i)
    queue = [s]
    # 모든정점에 대해
    while queue:
        x = queue.pop(0)
        # D[w]가 최소인 정점 w 선택
        if graph.get(x):
            for i in sorted(graph.get(x).items(), key=lambda x: x[1]):
                if not U.get(i[0]):
                    w = i[0]
                    queue.append(w)
                    U[w] = 1
        else:
            continue
        # w에 인접한 모든 정점 v
        for v in graph.get(x).keys():
            D[v] = min(D.get(v), D.get(x) + graph.get(x).get(v))

    return D


for tc in range(1, 1 + int(input())):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    graph = {chr(x): {} for x in range(ord('a'), ord('a') + N)}

    for i in range(E):
        u, v, w = input().split()
        if graph.get(u):
            if graph.get(u).get(v):
                graph[u][v].add(int(w))
            else:
                graph[u][v] = int(w)
        else:
            graph[u] = {v: int(w)}

    # print(graph)
    res = dijkstra('a')
    ans = [res.get(i) for i in sorted(graph)]
    print('#{} {}'.format(tc, ' '.join(map(str, ans))))
