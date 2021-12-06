# 15721. 번데기

import sys
input = sys.stdin.readline

a = int(input())
t = int(input())
target = int(input())
# 뻔-데기-뻔-데기-뻔-뻔-데기-데기
# 01010011
bdk = ''
cnt = 2
while len(bdk) < a*t:
    temp = '0101'
    temp += '0' * cnt + '1' * cnt
    cnt += 1
    bdk += temp

ans = 0
for i in range(len(bdk)):
    if bdk[i] == str(target):
        ans += 1
        if ans == t:
            print(i % a)
            break
