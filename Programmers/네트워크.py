from collections import deque

def bfs(a, visited, adj):
    q = deque([a])
    while q:
        x = q.popleft()
        visited[x] = 1
        for y in adj[x]:
            if not visited[y]:
                q.append(y)


def solution(n, computers):
    answer = 0
    adj = [[] for _ in range(n+1)]
    for i in range(n):
        computers[i][i] = 0
    
    visited = [0] * (n+1)
    for i in range(n):
        for j in range(n):
            if i==j: continue
            if computers[i][j]:
                adj[i].append(j)
    
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, adj)
            answer+=1
            
    return answer