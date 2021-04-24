# 1753. 최단거리
'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''

'''
0
2
3
7
INF
'''
import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(s):
    # U = {s: 1}
    d = [INF] * (N+1)
    # for a, b in adj[s]:
    #     d[a] = b
    d[s] = 0
    hq = []
    heapq.heappush(hq, (0, s))
    while hq:
        k, u = heapq.heappop(hq)
        for w, cost in adj[u]:
            if cost + d[u] < d[w]:
                d[w] = cost + d[u]
                heapq.heappush(hq,(d[w],w))

    # for _ in range(N+1):
    #     minV = INF
    #     for idx, value in enumerate(d):
    #         if not U.get(idx) and minV > value:
    #             minV = value
    #             min_idx = idx
    #             continue

    #     U[min_idx] = 1

    #     for e, w in adj[min_idx]:
    #         d[e] = min(d[e], d[min_idx] + w)

    return d


N, E = map(int, input().split())
k = int(input())
adj = {i: [] for i in range(1, N+1)}
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append([v, w])

for i in dijkstra(k)[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)