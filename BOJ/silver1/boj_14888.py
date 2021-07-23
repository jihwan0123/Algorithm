# 14888. 연산자 끼워넣기

import sys
input = sys.stdin.readline


calc = {
    0: lambda x, y: x + y,
    1: lambda x, y: x - y,
    2: lambda x, y: x * y,
    3: lambda x, y: abs(x) // y
}


def dfs(a, s):
    global max_ans, min_ans
    if a == n-1:
        max_ans = max(s, max_ans)
        min_ans = min(s, min_ans)
        return

    for i in range(4):
        if oper[i]:
            oper[i] -= 1
            if s < 0 and i == 3: # 음수일때 나누면 - 곱해준다.
                dfs(a+1, -calc[i](s, nums[a+1]))
            else:
                dfs(a+1, calc[i](s, nums[a+1]))
            oper[i] += 1


n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))
max_ans = -10e9
min_ans = 10e9

dfs(0, nums[0])
print(max_ans)
print(min_ans)
