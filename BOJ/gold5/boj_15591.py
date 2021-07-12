# 15591. MooTube(Silver)

import sys
from collections import deque
input = sys.stdin.readline


def bfs(k, v):
    visited = [0] * (n+1)
    queue = deque()
    queue.append((v, 0))
    cnt = 0
    while queue:
        nv, usado = queue.popleft()
        for next, next_usado in adj[nv]:  # 연결된 노드 돌면서 확인
            if not visited[next] and next_usado >= k:  # 방문 안하고 usado가 k보다 크면
                visited[nv] = 1
                queue.append((next, next_usado))  # nv와 연결된 정점 추가
                cnt += 1  # 연결되는 노드 갯수 카운팅

    return cnt


n, q = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(1, n):
    # p, q (동영상) , r(usado) / p와 q가 USADO r로 연결되어 있다. = 양방향 그래프
    a, b, r = map(int, input().split())
    adj[a].append((b, r))
    adj[b].append((a, r))


# i번째 질문이 K=k_j 라면 동영상 v_i 를 보고있는 소들에게 몇 개의 동영상이 추천될 지 묻는 것
for _ in range(q):
    k, v = map(int, input().split())
    print(bfs(k, v))  # bfs결과 연결된 노드의 수 출력
