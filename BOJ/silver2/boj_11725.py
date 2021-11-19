# 11725. 트리의 부모 찾기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
arr = [[] for _ in range(n+1)]
parents = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(s):
    for i in arr[s]:
        if not parents[i]:
            parents[i] = s
            dfs(i)


dfs(1)
for x in parents[2:]:
    print(x)
