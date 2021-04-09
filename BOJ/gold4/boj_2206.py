# 2206. 벽 부수고 이동하기

import sys

sys.stdin= open('boj_2206.txt')

dxy = [[0,1],[1,0],[-1,0],[0,-1]]
'''
# recursion error
sys.setrecursionlimit(10**6)

def dfs(x, y, cnt, check):
    if x == n-1 and y == m-1:
        global ans
        if ans > cnt:
            ans = cnt
        return
    if cnt > ans:
        return

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if nx >= n or ny >= m or ny < 0 or nx < 0: 
            continue
        # 비어있으면
        if not maps[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt+1, check)
            visited[nx][ny] = 0
        elif maps[nx][ny] and not visited[nx][ny] and check:
            check = 0
            visited[nx][ny] = 1
            dfs(nx, ny, cnt+1, check)
            visited[nx][ny] = 0
        

n, m = map(int, input().split())
# n개의 줄에 m개의 숫자 맵
maps = [list(map(int,input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
ans = 999999

dfs(0,0,1,1)
if ans == 999999:
    ans = -1
print(ans)
'''
'''
# 시간초과
def bfs():
    while queue:
        x, y, check, cnt = queue.pop(0)
        visited[x][y] = cnt
        if x == n-1 and y == m-1:
            global ans
            if ans > cnt:
                ans = cnt
        if cnt > ans:
            continue

        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y
            if nx >= n or ny >= m or ny < 0 or nx < 0: continue
            if not maps[nx][ny] and not visited[nx][ny]:
                queue.append((nx,ny,check,cnt+1))
            elif maps[nx][ny] and not visited[nx][ny] and check:
                check = 0
                queue.append((nx,ny,check,cnt+1))
                
        
n, m = map(int, input().split())
# n개의 줄에 m개의 숫자 맵
maps = [list(map(int,input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
ans = 999999
queue = [(0,0,1,1)]

bfs()
if ans == 999999:
    ans = -1


print(ans)
'''
'''
def bfs():
    while queue:
        x, y, check = queue.pop(0)
        if x == n-1 and y == m-1:
            return visited[x][y]

        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y
            if nx >= n or ny >= m or ny < 0 or nx < 0: continue
            if maps[nx][ny] and check:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny,0))

            elif not maps[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny,check))

    return -1
                
        
n, m = map(int, input().split())
maps = [list(map(int,input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
queue = [(0,0,1)]
print(bfs())
for i in visited:
    print(*i)
'''

def bfs():
    queue = [(0,0,1)]

    while queue:
        x, y, z = queue.pop(0)
        if x == n-1 and y == m-1:
            return visited[x][y][z]

        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y
            if nx >= n or ny >= m or ny < 0 or nx < 0: continue
            # 벽 뚫을 수 있으면
            if maps[nx][ny] and z == 1:
                visited[nx][ny][0] = visited[x][y][1] + 1
                queue.append((nx,ny,0))
            # 뚫고 왔고 벽이 아니면
            elif not maps[nx][ny] and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx,ny,z))
    return -1

           
n, m = map(int, input().split())
# n개의 줄에 m개의 숫자 맵
maps = [list(map(int,input())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
# visited[x][y][z]
# x,y 좌표, z: 뚫고왔는지 아닌지
visited[0][0][1] = 1

print(bfs())
for i in visited:
    print(*i)
