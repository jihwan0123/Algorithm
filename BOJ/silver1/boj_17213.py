# 17213. 과일 서리

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())


def fact(k):
    x = 1
    for i in range(1, k+1):
        x *= i
    return x


def combi(n, r):
    return fact(n) // (fact(r) * fact(n-r))


# H(n,r) = C(n+r-1,r)
m -= n
print(combi(n+m-1, m))
