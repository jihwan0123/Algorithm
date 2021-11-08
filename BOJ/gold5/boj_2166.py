# 2166. 다각형의 면적

import sys
input = sys.stdin.readline

n = int(input())
dots = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n-1):
    ans += dots[i][0] * dots[i+1][1] - dots[i+1][0] * dots[i][1]
ans += dots[n-1][0] * dots[0][1] - dots[0][0] * dots[n-1][1]
print(round(abs(ans/2), 1))
