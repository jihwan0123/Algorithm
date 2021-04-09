# 2178. 미로 탐색

import sys

sys.stdin= open('boj_2178.txt')

dxy = [[0,1],[1,0],[-1,0],[0,-1]]

def bfs():
    while queue:
        x, y = queue.pop(0)
        if x == n-1 and y == m-1:
            return visited[x][y]

        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y
            if nx >= n or ny >= m or ny < 0 or nx < 0: continue
            if maps[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

    return -1
                
        
n, m = map(int, input().split())
maps = [list(map(int,input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
queue = [(0,0)]
print(bfs())