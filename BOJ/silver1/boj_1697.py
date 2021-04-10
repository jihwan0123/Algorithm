# 1697. 숨바꼭질
from collections import deque

def bfs():
    # q = [N]
    q = deque()
    q.append(N)
    while q:
        # x = q.pop(0)
        x = q.popleft()
        # 찾았으면 종료
        if x == K:
            return visited[K]
        # -1, +1, *2 모두 저장 후 방문 한 곳까지 최단 시간 기록
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < 100001 and not visited[nx]:
                visited[nx] = visited[x]+1
                q.append(nx)
            

N, K = map(int, input().split())
# N : 수빈, K: 동생
visited = [0] * 100001
print(bfs())
