# 1966. 프린터 큐

import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    importance = deque()
    maxV = 0
    for idx, value in enumerate(imp):
        importance.append([idx, value])
        maxV = max(value, maxV)
    cnt = 0
    while importance:
        i, v = importance.popleft()
        if v == maxV: # 최댓값이면 제거
            cnt += 1
            if i == m:
                # 찾는 idx와 같으면 종료
                print(cnt)
                break
            else: # 다르면
                # 최댓값 갱신
                maxV = sorted(importance, key=lambda x: -x[1])[0][1]

        else: # 아니면 맨 뒤에 추가
            importance.append((i, v))
