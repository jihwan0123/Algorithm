# 14289. 본대 산책3

import sys
input = sys.stdin.readline
MOD = 1000000007

# 행렬 곱셈


def multiply(x, y, n):
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][k] = (temp[i][k] + x[i][j] * y[j][k]) % MOD

    return temp


n, m = map(int, input().split())
arr = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

D = int(input())

ans = [[0]*n for _ in range(n)]
for i in range(n):
    ans[i][i] = 1

while D:
    # 홀수면
    if D & 1:
        # ans 곱하고
        ans = multiply(ans, arr, n)
    # 짝수면
    D //= 2
    # 배열 제곱
    arr = multiply(arr, arr, n)


print(ans[0][0])
