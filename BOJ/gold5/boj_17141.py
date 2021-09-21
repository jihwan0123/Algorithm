# 17141. 연구소2

from collections import deque
from itertools import combinations
import sys
import copy
input = sys.stdin.readline


def bfs(selected_virus):
    maxV = 0
    labs_temp = copy.deepcopy(labs) # 2차원 배열 deepcopy
    for i in selected_virus:
        labs_temp[i[0]][i[1]] = 1 # 선택한 바이러스 위치 벽으로 바꿈
    visited = [[0] * n for _ in range(n)] # 방문 표시할 리스트
    # 선택한 바이러스부터 BFS
    while selected_virus:
        x, y, cnt = selected_virus.popleft()
        visited[x][y] = cnt
        maxV = max(maxV, cnt) # 최댓값 갱신
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and labs_temp[nx][ny] == 0: # 방문하지 않았고, 빈칸인 곳이면
                labs_temp[nx][ny] = 2 # 바이러스 복제
                selected_virus.append([nx, ny, cnt + 1])

    for i in range(n):
        for j in range(n):
            if not (labs_temp[i][j] or visited[i][j]): # BFS 이후 둘 다 0이면 불가능
                return -1
    return maxV - 1 # 시작 값을 1로 뒀으므로 -1


dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, input().split())
labs = []
virus = deque()  # 바이러스 좌표
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 2:
            temp[j] = 0
            virus.append([i, j, 1])
    labs.append(temp)

combi = list(combinations(virus, m))
ans = 2500
for c in combi:
    x = bfs(deque(c))
    if x != -1:
        ans = min(ans, x)

if ans == 2500:
    print(-1)
else:
    print(ans)
