# 1005. ACM Craft

from collections import deque
import sys
input = sys.stdin.readline

# 위상정렬
def topology_sort(x):
    result = [0] * (n+1)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = cost[i]

    while q:
        now = q.popleft()
        for b in buildings[now]:
            indegree[b] -= 1
            result[b] = max(result[b], result[now] + cost[b])
            if indegree[b] == 0:
                q.append(b)
    return result[x]


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    buildings = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    cost = [0] + list(map(int, input().split()))

    for i in range(k):
        a, b = map(int, input().split())
        buildings[a].append(b)
        indegree[b] += 1

    w = int(input())
    print(topology_sort(w))
