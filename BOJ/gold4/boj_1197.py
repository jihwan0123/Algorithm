# 1197. 최소 스패닝 트리

'''
3 3
1 2 1
2 3 2
1 3 3

3
'''
# prim

INF = float('inf')

# def extract_min(v,d):
#     min_key = INF
#     min_idx = 0
#     for i in range(1, V+1):
#         if not v[i] and d[i] < min_key:
#             min_idx = i
#             min_key = d[i]
#     return min_idx

# def prim(s):
#     key = [INF] * (V+1)
#     key[s] = 0
#     visited = [0] * (V+1)
#     for _ in range(E):
#         u = extract_min(visited, key)
#         visited[u] = 1
        
#         for w, v in adj[u]:
#             if not visited[v]:
#                 key[v] = min(key[v], w)

#     return sum(key[1:])
import heapq

def prim(s):
    q = []
    visited = [0] * (V+1)
    visited[s] = 1
    d= 0
    cnt = 1
    for a in adj[s]:
        heapq.heappush(q,a)
    
    while q:
        weight, v = heapq.heappop(q)
        if not visited[v]:
            visited[v] = 1
            cnt += 1
            d += weight
            for a in adj[v]:
                heapq.heappush(q,a)
        if cnt == V:
            return d
    return 0

V, E = map(int,input().split())
adj = [[] for _ in range(V+1)]
for i in range(E):
    A, B, C = map(int, input().split())
    adj[A].append((C, B))
    adj[B].append((C, A))

print(prim(1))




'''
## kruskal
def find(p,x):
    while p[x] != x:
        x = p[x]
    return x


def union(p, a, b):
    a = find(p,a)
    b = find(p,b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


V, E = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(E)]
p = list(range(V+1))


graph.sort(key=lambda x:x[2])
count = 0
answer = 0

for a,b,c in graph:
    if find(p,a) == find(p,b):
        continue
    else:
        union(p,a, b)
        answer += c

print(answer)
'''