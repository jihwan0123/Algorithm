# 9012. 괄호

import sys
input = sys.stdin.readline

k = int(input())


def is_pair(b):
    for i in b:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


for _ in range(k):
    bracket = list(input().rstrip())
    stack = []
    if is_pair(bracket):
        print('YES')
    else:
        print('NO')
