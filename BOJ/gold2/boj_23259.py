# 23259. Celebrity

import sys
input = sys.stdin.readline

stars = {}
n = int(input())
ans = 0
for _ in range(n):
    e = int(input())

    # 인접 리스트 생성
    adj = [[] for _ in range(5)]
    for _ in range(e):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)

    # 각 노드마다 인접 노드에 연결된 노드의 개수를 저장한다.
    visited = [[] for _ in range(5)]
    for i in range(5):
        for j in adj[i]:
            visited[i].append(len(adj[j]))
        # 노드를 바꿔도 같으므로 중복 체크 하기 쉽도록 정렬
        visited[i].sort()
        # 정렬 이후 i번째 노드에 연결된 개수를 마지막에 추가해준다.
        visited[i].append(len(adj[i]))

    # dict에 저장하기 위해 str형식으로 join해서 저장
    x = ' '.join(map(str, sorted(visited)))
    stars[x] = stars.get(x, 0) + 1
print(stars)

for s in stars:
    # 1번만 나온 별이 완전한 별이므로 개수를 센다
    if stars[s] == 1:
        ans += 1

print(ans)
