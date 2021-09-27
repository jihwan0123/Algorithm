# 1516. 게임 개발

from collections import deque
import sys
input = sys.stdin.readline


def topology_sort():
    result = [0] * (n+1)
    q = deque()

    # 진입차수 0인것부터 추가
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = cost[i] # 차수 0인것은 cost 값으로 초기화
            
    while q:
        now = q.popleft()
        for b in buildings[now]:
            indegree[b] -= 1
            # 앞서 필요한 건물 짓는 시간 + 현재 건물 짓는 시간
            # 모든 건물을 먼저 지어야 하므로 min이 아닌 max 값으로 갱신해줘야 한다.
            result[b] = max(result[b],result[now] + cost[b]) 
            if indegree[b] == 0:
                q.append(b)
    return result


n = int(input())

buildings = [[] for _ in range(n+1)]  # 노드와 간선 정보
indegree = [0] * (n+1)  # 진입차수
cost = [0] * (n+1)  # 걸리는 시간

for i in range(1, n+1):
    temp = list(map(int, input().split()))[:-1]  # 맨 뒤에 -1 제외
    cost[i] = temp[0]
    building = temp[1:]

    for j in building:
        buildings[j].append(i)  # 이후에 지어질 수 있는 건물들 추가
        indegree[i] += 1  # i로 연결된 노드의 진입차수 증가

ans = topology_sort()
for a in ans[1:]:
    print(a)