# 17071. 숨바꼭질5

from collections import deque
import sys
input = sys.stdin.readline


def bfs(n, k):
    q = deque([n])
    visited = [[False]*500001 for _ in range(2)]
    visited[0][n] = True
    cnt = 0
    while q:
        flag = cnt % 2  # 현재 짝수번째인지 홀수번째인지

        if k > 500000:
            return -1

        if visited[flag][k]:  # 방문했으면, 현재 cnt 출력
            return cnt

        flag = ~flag  # 다음 이동할 flag는 반대로

        length = len(q)
        for _ in range(length):  # 현재 cnt번째 q에 들어있는 만큼만 반복
            me = q.popleft()
            for next in (me*2, me-1, me+1):  # *2, 1, -1
                # 방문하지 않았으면
                if 0 <= next <= 500000 and not visited[flag][next]:
                    # 방문처리하고 추가
                    visited[flag][next] = True
                    q.append(next)
        cnt += 1
        k += cnt

    return -1


N, K = map(int, input().split())
print(bfs(N, K))
