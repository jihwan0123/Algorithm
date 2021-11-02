# 23292. 코딩 바이오리듬

import sys
input = sys.stdin.readline

x = input()
n = int(input())
answer = ""
maxV = 0
dates = sorted([input() for _ in range(n)], reverse=True)
for birth in dates:
    b = c = d = 0
    for i in range(4):
        b += (int(x[i])-int(birth[i]))**2
    for j in range(4, 6):
        c += (int(x[j])-int(birth[j]))**2
    for k in range(6, 8):
        d += (int(x[k])-int(birth[k]))**2
    temp = b*c*d
    if temp >= maxV:
        maxV = temp
        answer = birth

print(answer)
