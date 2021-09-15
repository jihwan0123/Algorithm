# 17069. 파이프 옮기기 2

import sys
input = sys.stdin.readline

n = int(input())
pipes = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]

# dp[x][y][z] (x,y) 좌표, z (0 : 가로, 1: 세로, 2: 대각선)
# (0,0) (0,1) 에 파이프 가로로 놓여있는 상태로 시작
dp[0][1][0] = 1
# 첫 행은 가로로만 가능
for i in range(2,n):
    if pipes[0][i]: # 벽이 있으면 가로로 더 갈 필요 없으므로 종료
        break
    else:
        dp[0][i][0] = dp[0][i-1][0]

for i in range(1, n):
    for j in range(2, n): # 처음엔 가로로만 놓을 수 있으므로 2부터 시작
        if pipes[i][j]: # 벽이면 건너뛰기
            continue
        # 가로, 세로
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2] # 가로 : 왼쪽에서 연결하거나, 대각선에서 연결
        dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2] # 세로 : 바로 위에서 연결하거나, 대각선에서 연결
        # 대각선: 벽을 긁으면 안되므로, 가로, 세로도 벽이면 안된다.
        if not (pipes[i-1][j] + pipes[i][j-1]):
            dp[i][j][2] = sum(dp[i-1][j-1])

print(sum(dp[n-1][n-1]))
