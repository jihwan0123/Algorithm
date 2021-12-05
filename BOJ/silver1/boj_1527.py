# 1527. 금민수의 개수

import sys
input = sys.stdin.readline


def dfs(num):
    global ans
    if num > B:
        return
    if A <= num <= B:
        ans += 1
    dfs(num*10 + 4)
    dfs(num*10 + 7)


A, B = map(int, input().split())
ans = 0

# 4로 시작, 7로 시작하는 경우
dfs(4)
dfs(7)

print(ans)
