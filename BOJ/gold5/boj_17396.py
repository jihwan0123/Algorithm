# 17396. 백도어

import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums[-1] = 0 # 넥서스 있는 곳 이동 가능하도록 변경
adj = [[] for _ in range(n)]


def dijkstra():
    dist = [INF] * n
    q = []
    heapq.heappush(q, (0, 0))
    dist[0] = 0
    while q:
        w, cur = heapq.heappop(q)
        if dist[cur] < w:
            continue

        for next, next_w in adj[cur]:
            if dist[next] > w + next_w:
                dist[next] = w + next_w
                heapq.heappush(q, (dist[next], next))

    return dist[-1]


for _ in range(m):
    a, b, t = map(int, input().split())
    # 와드 있는곳 건너뜀
    if nums[a] or nums[b]:
        continue
    adj[a].append([b, t])
    adj[b].append([a, t])

ans = dijkstra()
print(ans if ans != INF else -1) # 이동 가능여부 체크
