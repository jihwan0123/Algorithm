# 2644. 촌수계산

import sys
from collections import deque
input = sys.stdin.readline


def bfs(v, end):
    q = deque([[v, 0]])
    visited = [0] * (n+1)

    while q:
        v, cnt = q.popleft()
        if v == end:
            return cnt

        for i in adj[v]:
            if not visited[i]:
                visited[v] = 1
                q.append([i, cnt+1])
    return -1


n = int(input())
s, e = map(int, input().split())
m = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

print(bfs(s, e))