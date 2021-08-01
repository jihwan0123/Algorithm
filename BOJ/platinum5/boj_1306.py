# 1306. 달려라 홍준
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
light = list(map(int, input().split()))  # 빛의 세기
ans = [0] * n
q = deque()
r = 2*m-1
for i in range(n):
    # 윈도우에 있는 값이 light[i] 보다 작으면 저장할 필요가 없으니 제거
    while q and q[-1][0] <= light[i]:
        q.pop()

    q.append((light[i], i))  # 현재 값 넣고

    while (i - q[0][1]) >= r:  # 윈도우 벗어나면 제거
        q.popleft()

    ans[i] = q[0][0]

print(' '.join(map(str, ans[r-1:])))

'''
9 5 
2 3 4 5 6 7 4 3 2

7

8 3 
1 1 2 3 4 5 6 7

4 5 6 7
'''
