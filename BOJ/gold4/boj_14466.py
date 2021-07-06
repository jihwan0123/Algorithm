# 14466. 소가 길을 건너간 이유6
import sys
from collections import deque
input = sys.stdin.readline

dxy = [(0, 1), (1, 0), (-1, 0), (0, -1)]
n, k, r = map(int, input().split())
roads = {}
for _ in range(r):  # 길 위치 dict로 저장
    r, c, rr, cc = map(int, input().split())
    r -= 1
    c -= 1
    rr -= 1
    cc -= 1
    if roads.get((r, c)):
        roads[(r, c)].append((rr, cc))
    else:
        roads[(r, c)] = [(rr, cc)]

    if roads.get((rr, cc)):
        roads[(rr, cc)].append((r, c))
    else:
        roads[(rr, cc)] = [(r, c)]

cows = []
for _ in range(k):  # 소의 위치
    r, c = map(int, input().split())
    cows.append((r-1, c-1))


def bfs(r, c, i): # r,c 시작 좌표, i: 소 체크할 시작 번호 (소의 쌍 중복 방지용)
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    visited[r][c] = 1
    q = deque()
    q.append((r, c))
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if roads.get((nx, ny)) and (x, y) in roads.get((nx, ny)):  # 길이 연결되어 있는 곳이면 이동안함
                    continue
                else:  # 연결되지 않았으면 방문표시하고 큐에 추가
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    for a in range(i, k): # 방문 못하는 곳에 있으면 만나지 못했으니 체크
        if not visited[cows[a][0]][cows[a][1]]:
            cnt += 1
    return cnt


res = 0
for i in range(k-1):
    cow_r = cows[i][0]
    cow_c = cows[i][1]
    res += bfs(cow_r, cow_c, i+1)

print(res)
