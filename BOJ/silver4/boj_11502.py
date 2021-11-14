# 11502. 세 개의 소수 문제

import sys
input = sys.stdin.readline


# 에라토스 테네스의 체, 1000까지 소수 구하기
check = [True]*1001
prime_numbers = []
for i in range(2, 1001):
    if check[i]:
        prime_numbers.append(i)
        for j in range(2*i, 1001, i):
            check[j] = False


def find_nums(num):  # 3개의 소수 찾기
    for i in prime_numbers:
        if i >= num:
            break
        for j in prime_numbers:
            if j >= num:
                break
            for k in prime_numbers:
                if i+j+k == num:
                    print(i, j, k)
                    return
                if k >= num:
                    break
    print(0)


t = int(input())
for _ in range(t):
    n = int(input())
    find_nums(n)
