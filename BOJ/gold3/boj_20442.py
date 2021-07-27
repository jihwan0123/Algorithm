# 20442. ㅋㅋ루ㅋㅋ
import sys
input = sys.stdin.readline

words = list(input().strip())
lk = []  # R의 왼쪽 K 갯수
rk = []  # R의 오른쪽 K 갯수
cnt = 0
for i in words:
    if i == 'K':
        cnt += 1
    else:
        lk.append(cnt)
cnt = 0
for i in words[::-1]:
    if i == 'K':
        cnt += 1
    else:
        rk.append(cnt)
rk.reverse()

l, r = 0, len(rk) - 1
res = 0
while l <= r:
    res = max(res, r - l + 1 + 2 * min(lk[l], rk[r]))
    if lk[l] < rk[r]:
        l += 1
    else:
        r -= 1
print(res)
