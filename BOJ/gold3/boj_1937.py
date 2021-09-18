# 1937. 욕심쟁이 판다

import sys
input = sys.stdin.readline

# sys.setrecursionlimit(10**6)
# 예제에서 dxy 순서에 따라 recursion error가 발생한다.
dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
n = int(input())
forests = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]


def dfs(a, b):
    if dp[a][b]:  # 이미 계산한 값이 있으면 종료
        return dp[a][b]

    dp[a][b] = 1  # 초기 값 1로 설정
    for dx, dy in dxy:  # 4방향 돌면서
        na, nb = a + dx, b + dy
        # 먹을 수 있으면
        if 0 <= na < n and 0 <= nb < n and (forests[na][nb] > forests[a][b]):
            # 4방향 dfs값 + 1과 현재 저장된 값 비교해서 큰 값 저장
            dp[a][b] = max(dp[a][b], dfs(na, nb) + 1)

    return dp[a][b]


ans = 1
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))  # 모든 위치 돌면서 최댓값 저장
print(ans)
