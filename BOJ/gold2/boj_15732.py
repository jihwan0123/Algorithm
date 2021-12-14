# 15732. 도토리 숨기기

import sys

input = sys.stdin.readline


def check(target):
    cnt = 0
    for start, end, step in rules:
        # 시작값이 더 작으면 다음 규칙 체크
        if target < start:
            continue
        # 같으면 + 1
        elif target == start:
            cnt += 1
        else:
            # 끝나는 값과, 체크하는 값 중 최솟값까지 도토리 채운다.
            x = min(end, target)
            # 도토리 개수 계산
            cnt += (x - start) // step + 1
    # d보다 작은지 체크
    return cnt < d


n, k, d = map(int, input().split())
rules = []
l = sys.maxsize
r = 0
for _ in range(k):
    a, b, c = map(int, input().split())
    l = min(l, a)  # 규칙 시작하는 최솟값 저장
    r = max(r, b)  # 규칙 끝나는 최댓값 저장
    rules.append([a, b, c])

# 이분탐색
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        l = mid + 1
    else:
        r = mid - 1

print(l)
