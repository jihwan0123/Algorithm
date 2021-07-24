# 14499. 주사위 굴리기

import sys
input = sys.stdin.readline

dxy = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]  # 1,2,3,4 : 동,서,북,남

n, m, x, y, k = map(int, input().split())
dice = [0] * 7
nums = [list(map(int, input().split())) for _ in range(n)]  # n*m 지도
commands = list(map(int, input().split()))  # 이동 명령


def move(c):
    global x, y
    nx = x + dxy[c][0]
    ny = y + dxy[c][1]
    if 0 <= nx < n and 0 <= ny < m:  # 지도 범위 벗어나면 실행x
        x, y = nx, ny
        if c == 1:  # 동쪽으로 이동 4 -> 1 -> 3 -> 6 -> 4
            if nums[x][y]:  # 이동한 칸에 쓰여있는 수가 0이 아니면 바닥에 있는 숫자 복사 + 0으로 변경
                temp = dice[1]
                dice[1] = dice[4]
                dice[4] = dice[6]
                dice[6] = nums[x][y]
                nums[x][y] = 0
                dice[3] = temp
                print(dice[1])
            else:  # 0이면 주사위에 있는값 바닥에 복사
                temp = dice[1]
                dice[1] = dice[4]
                dice[4] = dice[6]
                dice[6] = dice[3]
                dice[3] = temp
                nums[x][y] = dice[6]
                print(dice[1])

        elif c == 2:  # 서쪽으로 이동 3 -> 1 -> 4 -> 6 -> 3
            if nums[x][y]:
                temp = dice[1]
                dice[1] = dice[3]
                dice[3] = dice[6]
                dice[6] = nums[x][y]
                dice[4] = temp
                nums[x][y] = 0
                print(dice[1])
            else:
                temp = dice[1]
                dice[1] = dice[3]
                dice[3] = dice[6]
                dice[6] = dice[4]
                dice[4] = temp
                nums[x][y] = dice[6]
                print(dice[1])

        elif c == 3:  # 북쪽으로 이동 1 -> 2 -> 6 -> 5 -> 1
            if nums[x][y]:
                temp = dice[1]
                dice[1] = dice[5]
                dice[5] = dice[6]
                dice[6] = nums[x][y]
                dice[2] = temp
                nums[x][y] = 0
                print(dice[1])
            else:
                temp = dice[1]
                dice[1] = dice[5]
                dice[5] = dice[6]
                dice[6] = dice[2]
                dice[2] = temp
                nums[x][y] = dice[6]
                print(dice[1])

        elif c == 4:  # 남쪽으로 이동 1 -> 5 -> 6 -> 2 -> 1
            if nums[x][y]:
                temp = dice[1]
                dice[1] = dice[2]
                dice[2] = dice[6]
                dice[6] = nums[x][y]
                dice[5] = temp
                nums[x][y] = 0
                print(dice[1])
            else:
                temp = dice[1]
                dice[1] = dice[2]
                dice[2] = dice[6]
                dice[6] = dice[5]
                dice[5] = temp
                nums[x][y] = dice[6]
                print(dice[1])


for c in commands:
    move(c)
