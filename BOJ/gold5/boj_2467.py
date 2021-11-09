# 2467. 용액

import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))
maxV = sys.maxsize
x = y = 0  # 두 용액
s = 0  # 시작지점
e = n-1  # 끝지점
while s < e:
    # 두 수의 합을 구하면서
    total = nums[s] + nums[e]
    # 현재 최댓값보다 작으면
    if (abs(total) < maxV):
        # 두 용액, 최댓값 갱신
        x = nums[s]
        y = nums[e]
        maxV = abs(total)
    # total이 음수면 왼쪽 포인터 오른쪽으로 1칸 이동
    if total < 0:
        s += 1
    else:  # 양수면 오른쪽 포인터 왼쪽으로 이동하면서 같아지면 종료
        e -= 1
print(x, y)
