# 4366. 정식이의 은행업무

import sys

sys.stdin = open('swea_4366.txt')

'''
def check(arr):
    global res
    for j in range(len(arr)):
        temp = list(arr)
        if temp[j] == 0:
            temp[j] = 1
            if pr2.get(int(''.join(map(str, temp)), 3)):
                return int(''.join(map(str, temp)), 3)
            temp[j] = 2
            if pr2.get(int(''.join(map(str, temp)), 3)):
                return int(''.join(map(str, temp)), 3)

        elif temp[j] == 1:
            temp[j] = 2
            if pr2.get(int(''.join(map(str, temp)), 3)):
                return int(''.join(map(str, temp)), 3)
            temp[j] = 0
            if pr2.get(int(''.join(map(str, temp)), 3)):
                return int(''.join(map(str, temp)), 3)

        elif temp[j] == 2:
            temp[j] = 0
            if pr2.get(int(''.join(map(str, temp)), 3)):
                return int(''.join(map(str, temp)), 3)

            temp[j] = 1
            if pr2.get(int(''.join(map(str, temp)), 3)):
                return int(''.join(map(str, temp)), 3)


for tc in range(1, 1 + int(input())):
    price2 = list(map(int, input()))
    price3 = list(map(int, input()))
    pr2 = {}
    for i in range(len(price2)):
        tmp = list(price2)
        tmp[i] = int(not tmp[i])
        pr2[(int(''.join(map(str, tmp)), 2))] = 1

    print(pr2)
    print('#%d %d' % (tc, check(price3)))
'''


def f(b, t):
    # bint = 0
    # for x in b:
    #     bint = bint * 2 + int(x)
    bint = int(b, 2)
    binary = []
    for i in range(len(b)):
        binary.append(bint ^ (1 << i))

    for i in range(len(t)):
        num1 = 0
        num2 = 0
        for j in range(len(t)):
            if i != j:
                num1 = num1 * 3 + int(t[j])
                num2 = num2 * 3 + int(t[j])
            else:
                num1 = num1 * 3 + (int(t[j]) + 1) % 3
                num2 = num2 * 3 + (int(t[j]) + 2) % 3

        if num1 in binary:
            return num1
        if num2 in binary:
            return num2


for tc in range(1, 1 + int(input())):
    pr2 = input()
    pr3 = input()
    print(f(pr2, pr3))
