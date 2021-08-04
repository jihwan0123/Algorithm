# 5014. 스타트링크

import sys
input = sys.stdin.readline



def bfs(start):
    visited = [0] * (F+1) # 전체 층수만큼 배열 생성
    visited[start] = 1 # 시작지점 방문체크
    q = [(start, 0)]
    while q:
        now, ans = q.pop(0)

        if now == G:
            return ans

        if now-D > 0 and not visited[now-D]:
            visited[now-D] = ans + 1
            q.append((now-D, ans + 1))
        if now+U <= F and not visited[now+U]:
            visited[now+U] = ans + 1
            q.append((now+U, ans + 1))
            
    return "use the stairs"


F, S, G, U, D = map(int, input().split())
print(bfs(S))
