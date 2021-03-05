# 1859. 백만 장자 프로젝트

import sys

sys.stdin = open('swea_1859.txt')

T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    price = list(map(int, input().split()))

    last = price[-1]
    # print(last)
    total = 0
    for i in range(len(price) - 1, -1, -1):  # 맨 뒤부터 비교
        if last > price[i]:  # 맨 뒤에 값이 그 앞 값보다 더 크면
            total += last - price[i]  # 두 수의 차이만큼 이득
            # print(total)
        else:  # 더 작으면 맨 뒤에 값에 넣어주고 비교 반복
            last = price[i]
            # print(last)
    print('#%d %d' % (tc, total))
