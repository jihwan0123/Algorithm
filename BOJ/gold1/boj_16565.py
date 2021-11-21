# 16565. N포커

import sys
input = sys.stdin.readline

num = int(input())
# 조합 저장
c = [[0]*53 for _ in range(53)]
for n in range(53):
    # nC0 = nCn = 1
    c[n][0] = c[n][n] = 1
    for k in range(1, n):
        # nCk = n-1Ck-1 + n-1Ck
        c[n][k] = (c[n-1][k-1] + c[n-1][k])

ans = 0
for i in range(4, num+1, 4):
    temp = i//4
    if temp & 1:  # 홀수면 더하고
        # 13개의 쌍에서 포카드 구하는 경우의 수 * 52-i개에서 num-i개 뽑는경우
        ans += c[13][temp] * c[52-i][num-i]
    else:  # 짝수면 뺀다.
        ans -= c[13][temp] * c[52-i][num-i]

print(ans % 10007)
