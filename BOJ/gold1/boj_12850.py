# 12850. 본대 산책2

import sys
input = sys.stdin.readline
MOD = 1000000007

# 연결 상태 배열
arr = [
    (0, 1, 1, 0, 0, 0, 0, 0),
    (1, 0, 1, 1, 0, 0, 0, 0),
    (1, 1, 0, 1, 1, 0, 0, 0),
    (0, 1, 1, 0, 1, 1, 0, 0),
    (0, 0, 1, 1, 0, 1, 0, 1),
    (0, 0, 0, 1, 1, 0, 1, 0),
    (0, 0, 0, 0, 0, 1, 0, 1),
    (0, 0, 0, 0, 1, 0, 1, 0)
]

# 행렬 곱셈
def multiply(x, y):
    temp = [[0]*8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                temp[i][k] = (temp[i][k] + x[i][j] * y[j][k]) % MOD

    return temp

# ans 배열 자기 자신으로 돌아오는 경우 1로 설정
ans = [[0]*8 for _ in range(8)]
for i in range(8):
    ans[i][i] = 1

D = int(input())
while D:
    # 홀수면
    if D & 1:
        # ans 곱하고
        ans = multiply(ans, arr)
    # 짝수면
    D //= 2
    # 배열 제곱
    arr = multiply(arr, arr)


print(ans[0][0])
