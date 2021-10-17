# 1647. 도시 분할 계획

import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())  # a와b 연결비용c
    adj[a].append((c, b))
    adj[b].append((c, a))


def prim(s):
    cnt = 1
    q = []
    visited = [0] * (n+1)
    visited[s] = 1
    for i in adj[s]:  # s와 연결된 노드들 저장
        heapq.heappush(q, i)

    while q:
        cost, node = heapq.heappop(q)
        if not visited[node]:  # 방문하지 않은 노드면
            visited[node] = cost  # 방문처리
            cnt += 1  # 방문한 갯수 1 증가
            if cnt == n:  # n개 다 연결했으면 visited 배열 return
                return visited
            for j in adj[node]:  # 방문하지 않은 노드에 연결된 노드들 heapq에 추가
                heapq.heappush(q, j)
    return -1


ans = prim(1)
ans[1] = 0
# 전체 더한 후 제일 긴 간선 제거하면 최솟값
print(sum(ans) - max(ans))
