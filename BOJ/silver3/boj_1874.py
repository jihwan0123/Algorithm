# 1874. 스택 수열

import sys
input = sys.stdin.readline

n = int(input())
stack = [0]
ans = []
cur = 1
for _ in range(n):
    x = int(input())
    # stack 마지막 값이 input과 같아질때까지 push
    while stack[-1] < x:
        stack.append(cur)
        ans.append('+')
        cur += 1
    # 같으면 pop하고 -
    if stack[-1] == x:
        stack.pop()
        ans.append('-')
    else:  # 아니면 불가능
        print('NO')
        sys.exit()

print('\n'.join(ans))
