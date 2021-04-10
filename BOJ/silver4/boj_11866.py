# 11866. 요세푸스0

from collections import deque

N, K = map(int, input().split())

dq = deque(range(1, N+1))
ans = []

while dq:
    dq.rotate(1-K)
    ans.append(dq.popleft())

res = '<' + str(ans)[1:-1] + '>'
print(res)
