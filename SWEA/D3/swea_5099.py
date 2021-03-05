# 5099. 피자굽기

import sys

sys.stdin = open('swea_5099.txt', 'r')


def bake_pizza(pizza):
    queue = list(range(N))
    temp = N
    while len(queue) > 1:
        i = queue.pop(0)
        Ci[i] //= 2
        if Ci[i]:
            queue.append(i)
        elif temp < M:
            queue.append(temp)
            temp += 1
    return queue[0] + 1


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    print('#{} {}'.format(tc, bake_pizza(Ci)))

'''
T = int(input())

for tc in range(1, 1 + T):
    N, M = map(int, input().split())  # N: 화덕의 크기, M: 피자의 갯수

    pizza = list(map(int, input().split()))  # 피자입력

    # 화덕생성
    firepot = []

    for i in range(N):
        firepot.append((i + 1, pizza[i]))

    # 피자를 N번부터 넣어야함
    next_pizza = N
    last_pizza = -1

    # while len(firepot) > 1:
    while firepot:
        num, cheese = firepot.pop(0)

        cheese //= 2
        last_pizza = num

        # 치즈의 양이 남아있다면
        if cheese:
            firepot.append((num, cheese))
        else:
            if next_pizza < M:
                firepot.append((next_pizza + 1, pizza[next_pizza]))
                next_pizza += 1

    print('#{} {}'.format(tc, last_pizza))
    # print('#{} {}'.format(tc, firepot[0][0]))
'''
