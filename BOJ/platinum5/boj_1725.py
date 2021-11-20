# 1725. 히스토그램

import sys
input = sys.stdin.readline

n = int(input())
h = [0] + [int(input()) for _ in range(n)] + [0]
stack = [0]
ans = 0
for i in range(1, n+2):  # 1부터 n+1까지 돌면서
    # stack의 마지막 값이 h의 높이보다 높으면
    while stack and h[stack[-1]] > h[i]:
        # stack에서 하나를 빼고
        top = stack.pop()
        # 최대 넓이 계산 후 갱신
        ans = max(ans, h[top] * (i-1-stack[-1]))
    # 현재 index값 stack에 저장
    stack.append(i)

print(ans)
