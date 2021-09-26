# 2252. 줄 세우기

from collections import deque
import sys
input = sys.stdin.readline


def topology_sort():
    result = []
    q = deque()
    # 진입차수 0인것 부터 큐에 추가
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        # 큐에서 꺼내서
        now = q.popleft()
        result.append(now)
        # 연결된 진입차수들 -1
        for j in graph[now]:
            indegree[j] -= 1
            # 진입차수 0이면 q에 추가
            if indegree[j] == 0:
                q.append(j)

    return result


n, m = map(int, input().split())
# 진입차수
indegree = [0] * (n + 1)
# 노드에 연결된 간선 정보
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # a에서 b로 이동 가능
    # 진입 차수 1 증가
    indegree[b] += 1

ans = topology_sort()
print(*ans)
