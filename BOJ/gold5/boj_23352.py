# 23352. 방탈출

from collections import deque
import sys
input = sys.stdin.readline


def bfs(a, b):
    visited = [[0] * m for _ in range(n)]
    q = deque([(a, b, 1)])
    temp = [rooms[a][b]]  # 최대 길이가 1일 수 있으므로 자기자신으로 시작
    visited[a][b] = 1
    ans = []
    while True:
        next = deque()
        # next : 다음에 이동할 좌표들, temp: 현재 이동한 방의 크기
        while q:
            x, y, cnt = q.popleft()
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and rooms[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = cnt + 1
                    next.append((nx, ny, cnt+1))
                    temp.append(rooms[nx][ny])
        # 이동할 곳이 있으면
        if temp:
            # 현재까지 이동한 크기와 길이 더하고
            ans.append([max(temp)+rooms[a][b], cnt+1])
            # 다음 q에 넣고
            q = next
            # temp 초기화
            temp.clear()
            continue
        # 가장 마지막에 이동한 방 return
        return ans[-1]


n, m = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(n)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
res = []
for i in range(n):
    for j in range(m):
        # 0이 아닌곳부터 시작
        if rooms[i][j]:
            res.append(bfs(i, j))
# 길이순, 크기순으로 정렬 후 첫번째 값
print(sorted(res, key=lambda x: (x[1], x[0]), reverse=True)[0][0])
