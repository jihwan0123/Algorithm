# 5430. AC

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
ans = []
for _ in range(t):
    p = input()
    n = int(input())
    x = input().strip().lstrip('[').rstrip(']').split(',')
    rev = 0
    if p.count('D') > n:
        ans.append('error')
        continue
    elif p.count('D') == n:
        ans.append('[]')
        continue

    if x[0]:
        x = deque(map(int, x))
    else:
        ans.append('error')
        continue

    for i in p:
        if i == 'R':
            rev = 1-rev
        elif i == 'D':
            if rev:
                x.pop()
            else:
                x.popleft()

    if rev:
        x.reverse()
        ans.append('[' + ','.join(map(str, x)) + ']')
    else:
        ans.append('[' + ','.join(map(str, x)) + ']')


print('\n'.join(ans))
