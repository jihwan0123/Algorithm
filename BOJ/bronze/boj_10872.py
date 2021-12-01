# 10872. 팩토리얼

import sys
sys.setrecursionlimit(2000)


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)


print(fact(int(input())))
