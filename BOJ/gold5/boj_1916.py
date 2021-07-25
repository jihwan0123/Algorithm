# 1916. 최소비용 구하기

import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline


def dijkstra(start):
    d = [INF] * (N + 1)
    d[start] = 0
    hq = [(0, start)]

    while hq:
        weight, node = heapq.heappop(hq)
        if d[node] < weight:  # 경로 같은데 비용이 다른 경우도 있을 수 있다.(안해주면 시간초과)
            continue
        for e, c in adj[node]:
            if d[e] > weight + c:
                d[e] = weight + c
                heapq.heappush(hq, (d[e], e))
    return d


N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append((e, w))

x, y = map(int, input().split())

print(dijkstra(x)[y])
