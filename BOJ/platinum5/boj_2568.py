# 2568. 전깃줄 - 2

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)])
temp = []  # LIS 저장
check = []  # 모든 문자에 대해 최장 길이 저장

# LIS 구하면서 각 문자에 대한 최장 길이 저장
for a, x in arr:
    if not temp or temp[-1] < x:
        temp.append(x)
        check.append(len(temp))
    else:
        idx = bisect_left(temp, x)
        temp[idx] = x
        check.append(idx+1)

length = len(temp)  # length = LIS 길이
res = {}
# check 배열 역방향으로 체크
for i in range(len(check)-1, -1, -1):
    # 최장길이부터 내려오면서 체크하면서 문자열 저장
    if check[i] == length:
        res[arr[i][0]] = True
        length -= 1

    if length == 0:
        break

ans = []
for a, x in arr:
    if res.get(a):
        continue
    ans.append(a)

print(len(ans))
print('\n'.join(map(str, ans)))
