# 2606. 바이러스

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


def bfs(s):
    q = [s]
    visited = [0] * (n+1)
    while q:
        x = q.pop(0)
        visited[x] = 1
        for i in adj[x]:
            if not visited[i]:
                q.append(i)

    return visited.count(1)


print(bfs(1)-1)
