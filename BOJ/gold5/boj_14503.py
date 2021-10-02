# 14503. 로봇 청소기

from collections import deque
import sys
input = sys.stdin.readline


def cleaning(a, b, c):
    q = deque([(a, b, c)])
    while q:
        chk = False  # 청소할 곳 찾았는지
        x, y, d = q.popleft()
        # 1. 현재위치 청소
        cleaned[x][y] = 1
        # 2. 현재 방향 기준으로 왼쪽부터 인접한 칸 탐색
        for i in range(1, 5):
            nx, ny = x + dxy[(d+i) % 4][0], y + dxy[(d+i) % 4][1]
            # 벽이 아니고 청소 안했으면
            if not regions[nx][ny] and not cleaned[nx][ny]:
                # 왼쪽이 청소하지 않았으면 회전후 한칸 전진후 1번으로
                chk = True
                q.append((nx, ny, (d+i) % 4))
                break
            # 청소했으면 한번 더 왼쪽으로 회전

        # 청소할 곳 못찾았으면
        if not chk:
            # 청소할 수 있는 곳이 없으면 마지막 방향 바라본채로 뒤로 1칸이동
            nx, ny = x - dxy[d][0], y - dxy[d][1]
            # 후진은 벽인지만 체크, 청소여부는 관계 없음
            if not regions[nx][ny]:
                q.append((nx, ny, d))

        # 뒤로 돌아갈 수 없으면 종료


dxy = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 서, 남, 동, 북

direction = {0: 3, 1: 2, 2: 1, 3: 0}

n, m = map(int, input().split())
r, c, d = map(int, input().split())  # (r,c) d방향
dis = direction.get(d)  # 초기 방향 설정

regions = [list(map(int, input().split())) for _ in range(n)]  # 벽인지 아닌지
cleaned = [[0] * m for _ in range(n)]  # 청소 여부

cleaning(r, c, dis)

ans = 0
for v in cleaned:
    ans += v.count(1)
print(ans)
