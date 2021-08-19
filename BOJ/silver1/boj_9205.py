# 9205. 맥주마시면서 걸어가기

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    visited = dict()
    visited[(x, y)] = True
    while q:
        x, y = q.popleft()
        if (x, y) == (end_x, end_y):  # 도착했으면 happy
            print("happy")
            return
        for nx, ny in locations:  # 전체 위치중에
            # 방문 안한 좌표중에서 맥주가 없어지기 전에 이동할 수 있으면
            if not visited.get((nx, ny)) and (abs(nx-x) + abs(ny-y) <= 1000):
                # 추가하고 방문처리
                q.append((nx, ny))
                visited[(nx, ny)] = True
    print("sad")


t = int(input())
for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())  # 시작지점
    locations = [list(map(int, input().split())) for _ in range(n+1)]  # 편의점 + 도착지점
    end_x, end_y = locations[-1][0], locations[-1][1]  # 도착지점
    bfs(start_x, start_y)
