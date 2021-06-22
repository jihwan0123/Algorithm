# 1260. DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline


def dfs(s):
    for i in adj[s]:
        if not dfs_visited[i]:
            if i not in dfs_res:
                dfs_res.append(i)
                dfs(i)

def bfs(s):
    queue = deque()
    queue.append(s)
    bfs_res = []
    bfs_visited = [0] * (n+1)
    while queue:
        x = queue.popleft()
        if x not in bfs_res:
            bfs_res.append(x)
            for i in adj[x]:
                if not bfs_visited[i]:
                    queue.append(i)

    return ' '.join(map(str, bfs_res))


n, m, v = map(int, input().split())
dfs_res = [v]
dfs_visited = [0] * (n+1)
dfs_visited[v] = 1

adj = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for a in adj:
    a.sort()

dfs(v)
print(*dfs_res)
print(bfs(v))
