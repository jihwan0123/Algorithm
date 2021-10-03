# 10971. 외판원 순회2

import sys
input = sys.stdin.readline


def dfs(s, cur, lev, total):  # s: 시작지점, cur: 현재위치, lev: 지나온 레벨, total : 현재까지 비용 합
    global min_cost

    if total >= min_cost:
        return

    if lev >= n:
        if costs[cur][s]:
            min_cost = min(min_cost, total + costs[cur][s])
        return

    for i in range(n):
        if visited[i]: continue # 방문했으면 넘어감
        if costs[cur][i]: # 이동할 수 있으면
            visited[i] = 1 # 방문처리하고
            dfs(s, i, lev + 1, total + costs[cur][i]) # 이동
            visited[i] = 0 # 방문취소 후 반복


n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
min_cost = sys.maxsize
visited = [0] * (n+1)

for i in range(n):
    visited[i] = 1
    dfs(i, i, 1, 0)
    visited[i] = 0


print(min_cost)
