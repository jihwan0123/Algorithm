# 1021: 장난감조립
import sys
input = sys.stdin.readline


def dfs(lev, cnt):
    for a, b in adj[lev]:
        res[a] += b * cnt
        if adj[a]:
            dfs(a, cnt*b)


n = int(input())
m = int(input())
res = [0] * (n+1)
adj = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, k = map(int, input().split())
    adj[x].append((y, k))


dfs(n, 1)
for i in range(1, n):
    if not adj[i]:
        print(i, res[i])
