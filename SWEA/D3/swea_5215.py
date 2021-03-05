# 5215. 햄버거 다이어트

import sys

sys.stdin = open('swea_5215.txt')


def combination(start, cal, point):
    # level : 재료 수
    # cal : 칼로리 합, rank : 맛 점수
    global total

    if total < point:
        total = point

    for i in range(start, N):
        # 기댓값과 현재값을 더한게 더 작거나 같으면 종료
        # 가지치기 1 (중요)
        if expect[i] + point <= total: break
        # 가지치기 2
        # 칼로리가 최대치를 넘어서면 다음꺼 확인
        if cal + cals[i] >= L: continue
        combination(i + 1, cal + cals[i], point + points[i])


T = int(input())

for tc in range(1, 1 + T):
    N, L = map(int, input().split())
    # N : 재료의 수, L: 제한칼로리
    mk = [tuple(map(int, input().split())) for _ in range(N)]
    total = 0
    points = [mk[n][0] for n in range(N)]
    cals = [mk[n][1] for n in range(N)]

    expect = [0] * N
    expect[N - 1] = points[N - 1]

    # x 번째부터 뒤에꺼를 다 선택했을때 나올 수 있는 최댓값 저장
    # [1 2 2 3 1] expect [9 8 6 4 1]
    for x in range(N - 2, -1, -1):
        expect[x] = expect[x + 1] + points[x]

    combination(0, 0, 0)
    print('#{} {}'.format(tc, total))
