# 17615. 볼 모으기

import sys
input = sys.stdin.readline

n = int(input())
balls = input().strip()
red = balls.count('R')
blue = n-red
# n이면 0번
if red == n or blue == n:
    print(0)
else:
    '''
    # red, blue중 작은 수로 초기화
    ans = min(red, blue)
    cnt_left = 0
    # 왼쪽으로 정렬
    for i in range(n):
        # 연속인 갯수 체크
        if balls[i] != balls[0]:
            break
        cnt_left += 1

    # 처음 시작이 R이면
    if balls[0] == 'R':
        # red-cnt번 이동으로 왼쪽으로 옮기기 가능
        ans = min(ans, red-cnt_left)
    else:
        # B면 blue-cnt번
        ans = min(ans, blue-cnt_left)

    cnt_right = 0
    # 오른쪽으로 정렬
    for i in range(n-1, -1, -1):
        if balls[i] != balls[-1]:
            break
        cnt_right += 1

    if balls[-1] == 'R':
        ans = min(ans, red-cnt_right)
    else:
        ans = min(ans, blue-cnt_right)
    '''
    # find 메소드로 간단히 가능
    ans = min(red, blue)
    if balls[0] == 'R':
        ans = min(ans, red-balls.find('B'))
    else:
        ans = min(ans, blue-balls.find('R'))

    if balls[-1] == 'R':
        ans = min(ans, red-balls[::-1].find('B'))
    else:
        ans = min(ans, blue-balls[::-1].find('R'))
    print(ans)
