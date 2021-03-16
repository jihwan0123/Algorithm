# 4008. [모의 SW 역량테스트] 숫자 만들기

import sys

sys.stdin = open('swea_4008.txt')

# 계산용 dict
calc = {0: (lambda a, b: a + b),
        1: (lambda a, b: a - b),
        2: (lambda a, b: a * b),
        3: (lambda a, b: int(a / b))
        }


# 연산자 순서별로 다 돌아보기 위한 dfs
def dfs(idx, res):
    if idx >= n:
        global res_min, res_max
        if res_min > res:
            res_min = res
        if res_max < res:
            res_max = res
        return
    # 앞에서부터 하나씩 빼면서 반복
    for i in range(4):
        # 연산자가 있으면
        if operator[i]:
            # 하나 빼고
            operator[i] -= 1
            # dfs 반복
            dfs(idx + 1, calc[i](res, nums[idx + 1]))
            # 다시 더해줘서 for문 반복
            operator[i] += 1


for tc in range(1, 1 + int(input())):
    N = int(input())
    n = N - 1
    operator = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    res_min = 987654321
    res_max = -987654321
    dfs(0, nums[0])
    print('#{} {}'.format(tc, res_max - res_min))
