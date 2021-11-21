# 6549. 히스토그램에서 가장 큰 직사각형

import sys
input = sys.stdin.readline

while True:
    n, *x = list(map(int, input().split()))
    if n == 0:
        break
    h = [0] + x + [0]
    stack = [0]
    ans = 0
    for i in range(1, n+2):
        while stack and h[stack[-1]] > h[i]:
            top = stack.pop()
            ans = max(ans, h[top] * (i-1-stack[-1]))
        stack.append(i)

    print(ans)
