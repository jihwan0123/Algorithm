# 10984. 내 학점을 구해줘

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = [tuple(map(float, input().split())) for _ in range(n)]
    x = sum(a[i][0] for i in range(n))
    y = sum(a[i][0] * a[i][1] for i in range(n))
    print(int(x), round(y/x, 1))
