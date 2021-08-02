# 21924. 도시 건설

import sys
from heapq import *
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
total = 0
for _ in range(m):
    a, b, c = map(int, input().split())  # a와b  연결비용c
    total += c  # 총합
    adj[a].append((c, b))
    adj[b].append((c, a))


def prim(s):
    res, cnt = 0, 1
    q = []
    visited = [0] * (n+1)
    visited[s] = 1
    for i in adj[s]:  # s와 연결된 노드들 저장
        heappush(q, i)

    while q:
        cost, node = heappop(q)
        if not visited[node]:  # 방문하지 않은 노드면
            visited[node] = 1  # 방문처리하고
            res += cost  # cost 더해주고
            cnt += 1  # 방문한 갯수 1 증가
            for j in adj[node]:  # 방문하지 않은 노드에 연결된 노드들 heapq에 추가
                heappush(q, j)

        if cnt == n:  # n 개 다 연결했으면 도로의 총합 return
            return res
    return -1


ans = prim(1)
if ans == -1:
    print(ans)
else:
    print(total - ans)
