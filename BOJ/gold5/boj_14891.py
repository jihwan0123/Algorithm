# 14891. 톱니바퀴

import sys
from collections import deque
input = sys.stdin.readline

topni1 = deque(input().strip())
topni2 = deque(input().strip())
topni3 = deque(input().strip())
topni4 = deque(input().strip())

k = int(input())  # 회전횟수
commands = [list(map(int, input().split())) for _ in range(k)]
ans = 0


for command in commands:
    x, y = command[0], command[1]
    if x == 1:
        if topni1[2] != topni2[6]:
            if topni2[2] != topni3[6]:
                if topni3[2] != topni4[6]:
                    topni4.rotate(-y)
                topni3.rotate(y)
            topni2.rotate(-y)
        topni1.rotate(y)

    elif x == 2:
        if topni1[2] != topni2[6]:
            topni1.rotate(-y)
        if topni2[2] != topni3[6]:
            if topni3[2] != topni4[6]:
                topni4.rotate(y)
            topni3.rotate(-y)
        topni2.rotate(y)

    elif x == 3:
        if topni3[2] != topni4[6]:
            topni4.rotate(-y)
        if topni3[6] != topni2[2]:
            if topni2[6] != topni1[2]:
                topni1.rotate(y)
            topni2.rotate(-y)
        topni3.rotate(y)

    elif x == 4:
        if topni3[2] != topni4[6]:
            if topni2[2] != topni3[6]:
                if topni1[2] != topni2[6]:
                    topni1.rotate(-y)
                topni2.rotate(y)
            topni3.rotate(-y)
        topni4.rotate(y)

if topni1[0] == '1':
    ans += 1
if topni2[0] == '1':
    ans += 2
if topni3[0] == '1':
    ans += 4
if topni4[0] == '1':
    ans += 8

print(ans)
