# 2638. 치즈

from collections import deque
import sys
input = sys.stdin.readline


def bfs(a, b): # 제일 바깥 공기 -1로 변경, 인접한 치즈 + 1
    q = deque([(a, b)])
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if cheeses[nx][ny] == 0:
                    cheeses[nx][ny] = -1
                    q.append((nx, ny))
                elif cheeses[nx][ny] >= 1:
                    cheeses[nx][ny] += 1
                    if cheeses[nx][ny] == 3: # 인접한 공기가 2칸이면 지울것
                        cheese_list.append((nx, ny))


dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, input().split())
cheeses = [list(map(int, input().split())) for _ in range(n)]
cheese_list = deque()

bfs(0, 0) 
ans = 0
while cheese_list:
    ans += 1
    i = 0
    length = len(cheese_list)
    while i < length:
        x, y = cheese_list.popleft()
        cheeses[x][y] = -1
        bfs(x, y)
        i += 1


print(ans)
