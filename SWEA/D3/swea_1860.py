# 1860. 진기의 최고급 붕어빵

import sys

sys.stdin = open('swea_1860.txt')

for tc in range(1, 1 + int(input())):
    N, M, K = map(int, input().split())
    # N : 사람수, M초마다 K개 생산
    nums = list(map(int, input().split()))
    person = {}

    for i in nums:
        if person.get(i):
            person[i] += 1
        else:
            person[i] = 1

    people = sorted(person.items())
    # dict key(초) 기준으로 정렬
    
    total, bread = 0, 0
    # total: 전체 사람 수
    # bread: 만든 빵 갯수

    result = 'Possible'
    for a, b in people:
        total += b
        bread = int(a / M) * K

        if bread < total:
            result = 'Impossible'
            break

    print('#{} {}'.format(tc, result))
