# 11003. 최솟값 찾기

import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))  # A1, A2 ... AN
q = deque()
D = [0] * N
for i in range(N):
    # 윈도우에 있는 값이 A[i] 보다 크면 저장할 필요가 없으니 제거
    while q and q[-1][0] > A[i]:
        q.pop()

    q.append((A[i], i))  # 현재 값 넣고

    if (i - q[0][1]) >= L:  # L칸 넘어서 윈도우 벗어나면 제거
        q.popleft()
    D[i] = q[0][0]

print(' '.join(map(str, D)))
