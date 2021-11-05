# 4386. 별자리 만들기

import sys
input = sys.stdin.readline


def find_parent(x):
    if parent[x] == x:  # 본인이 루트 노드인 경우
        return x
    return find_parent(parent[x])  # 루트노드 return


def union(a, b):
    pa, pb = find_parent(a), find_parent(b)
    if pa == pb:  # 같으면 종료
        return

    if pa < pb:  # 다르면 노드값이 더 낮은 트리쪽으로 합치기
        parent[pb] = pa
    else:
        parent[pa] = pb


n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
edges = []
ans = 0
for a in range(n):
    for b in range(a+1, n):
        c = ((stars[a][0]-stars[b][0])**2 + (stars[a][1]-stars[b][1])**2)**0.5
        edges.append((c, a, b))

# 가중치 오름차순로 정렬
edges.sort()
# 루트 노드 자기자신에게 초기화
parent = list(range(n))
for cost, x, y in edges:
    # 부모노드가 다르면
    if find_parent(x) != find_parent(y):
        # 합치고
        union(x, y)
        # cost 더하기
        ans += cost

print(round(ans, 2))
