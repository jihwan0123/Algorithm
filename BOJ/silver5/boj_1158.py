# 1158. 요세푸스 문제

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = deque(list(range(1, n+1)))
ans = []
while arr:
    arr.rotate(-k+1)
    ans.append(arr.popleft())

print('<' + ', '.join(map(str, ans)) + '>')
