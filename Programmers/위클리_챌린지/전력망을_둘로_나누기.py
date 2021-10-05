# 전력망을 둘로 나누기
from collections import deque


def bfs(n, adj):
    visited = [False] * (n+1)
    cnt = 0
    q = deque([1])
    while q:
        v = q.popleft()
        cnt += 1
        visited[v] = True
        for i in adj[v]:
            if not visited[i]:
                q.append(i)
    return cnt


def solution(n, wires):
    answer = 987654321
    for i in range(len(wires)):
        # i번째 전선 제거한 adj 구하기
        adj = [[] for _ in range(n+1)]
        for j in range(len(wires)):
            if j == i:
                continue
            adj[wires[j][0]].append(wires[j][1])
            adj[wires[j][1]].append(wires[j][0])

        temp = bfs(n, adj)  # i번째 제거 후 1번 전선에서 연결된 노드 개수
        answer = min(answer, abs(n-2*temp)) # 최솟값 갱신

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
