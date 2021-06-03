# 1916. 최소비용 구하기

# input
'''
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
'''
# output: 4
import sys, heapq
input = sys.stdin.readline

def dijkstra(start, end):
    d = [sys.maxsize] * (N + 1)
    d[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        weight, node = heapq.heappop(hq)
        for e, c in adj[node]:
            if d[e] > weight + c:
                d[e] = weight + c
                heapq.heappush(hq, (d[e], e))
    return d[end]


N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append((e, w))

start, end = map(int, input().split())

print(dijkstra(start, end))