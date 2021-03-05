# 6485. 삼성시의 버스 노선

import sys

sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, 1 + T):
    n = int(input())

    bus_stop = [0] * 5001

    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a, b + 1):
            bus_stop[j] += 1

    p = int(input())

    c = []
    for i in range(p):
        j = input()
        c.append(int(j))

    sol = []
    for k in c:
        sol.append(bus_stop[k])

    print('#%d' % tc, end=' ')
    print(*sol)
