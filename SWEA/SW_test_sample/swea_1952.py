# 1952. [모의 SW 역량테스트] 수영장

import sys

sys.stdin = open('swea_1952.txt')


def swim(m, price):
    # m : 현재 월
    # price : 현재 지불 금액
    if m > 12:
        global result
        if price < result:
            result = price
        return

    # 1일권, 1달권
    swim(m + 1, price + min(month, plan[m - 1] * day))

    # 3달권
    swim(m + 3, price + three_month)


for tc in range(1, 1 + int(input())):
    day, month, three_month, year = map(int, input().split())
    plan = list(map(int, input().split()))
    result = year
    swim(1, 0)
    print('#{} {}'.format(tc, result))
