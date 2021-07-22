# 20055. 컨베이어 벨트 위의 로봇

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
belt = deque(map(int, input().split()))  # 벨트의 내구도
robot = deque([0] * (2*n))


def rotate(K):
    cnt = 1
    while True:
        # 1. 컨베이어 벨트 회전
        belt.rotate()
        robot.rotate()

        # n-1 번째 로봇 있으면 내린다.
        if robot[n-1]:
            robot[n-1] = 0

        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
        for i in range(n-1, 0, -1):  # n-1부터 0 순서로 올라갔다.
            # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
            if robot[i-1] and not robot[i] and belt[i]:
                robot[i] = robot[i-1]  # 로봇 한칸 이동
                robot[i-1] = 0  # 기존 칸 로봇 제거
                belt[i] -= 1  # 벨트 내구도 1 감소
            # 이동할 수 없다면 가만히 있는다.

        # 이동이 끝나고 n-1 번째 로봇이 있으면 내린다.
        if robot[n-1]:
            robot[n-1] = 0

        # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        if not robot[0] and belt[0]:
            # 올린다
            robot[0] = 1
            belt[0] -= 1

        # 4.내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료
        if belt.count(0) >= K:
            return cnt
        cnt += 1


print(rotate(k))
