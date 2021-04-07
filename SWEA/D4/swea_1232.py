# 1232. 사칙연산

import sys

sys.stdin = open('swea_1232.txt')

'''
def postorder(n):
    n = int(n)
    if n > 0:
        # left
        postorder(left[n])
        # 가운데
        postorder(right[n])
        # right
        res.append(tree[n - 1][1])


calc = {"+": (lambda a, b: a + b),
        "-": (lambda a, b: a - b),
        "*": (lambda a, b: a * b),
        "/": (lambda a, b: a // b)
        }


def calculation(data):
    stack = []
    for x in data:
        if x.isdigit():
            stack.append(int(x))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(calc[x](a, b))

    return stack[0]


for tc in range(1, 11):
    N = int(input())
    tree = [input().split() for _ in range(N)]
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    pa = [0] * (N + 1)

    for i in range(0, N):
        if len(tree[i]) == 4:
            left[i + 1] = int(tree[i][2])
            right[i + 1] = int(tree[i][3])

        elif len(tree[i]) == 3:
            left[i + 1] = int(tree[i][2])
    res = []
    for i in range(1, N + 1):
        if pa[i] == 0:
            root = i
            break

    postorder(root)
    result = calculation(res)
    print('#{} {}'.format(tc, result))
'''

calc = {"+": (lambda a, b: a + b),
        "-": (lambda a, b: a - b),
        "*": (lambda a, b: a * b),
        "/": (lambda a, b: a // b)
        }


def calculate(index):
    node = tree[index]
    if len(node) > 2:
        a, b = calculate(int(node[2])), calculate(int(node[3]))
        return calc[node[1]](a, b)
    return int(node[1])


for tc in range(1, 11):
    N = int(input())
    tree = [0] + [input().split() for _ in range(N)]
    res = []

    print('#{} {}'.format(tc, calculate(1)))
