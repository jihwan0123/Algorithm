# 1072. 게임

import sys

input = sys.stdin.readline

x, y = map(int, input().split())
ans = -1

# 같으면 종료
if x == y:
    print(ans)
    sys.exit()

z = (int)(100 * y / x)
l, r = 1, 1e9

# 이분탐색으로 ans 찾기
while l <= r:
    m = (l + r) // 2
    if (int)(100 * (y + m) / (x + m)) != z:
        ans = m
        r = m - 1
    else:
        l = m + 1

print(int(ans))
