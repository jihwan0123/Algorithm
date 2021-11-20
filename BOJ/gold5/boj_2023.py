# 2023. 신기한 소수

import sys
input = sys.stdin.readline


def is_prime(num):  # 소수 판별
    num = int(num)
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True


def dfs(cur, length):
    if length == n:
        print(int(cur))
        return
    for i in (1, 3, 7, 9):  # 1,3,7,9만 붙였을때 소수 가능
        if is_prime(cur+str(i)):
            dfs(cur + str(i), length + 1)


n = int(input())
for i in (2, 3, 5, 7):  # 한자리수 소수는 2,3,5,7뿐, 맨 앞자리 고정
    dfs(str(i), 1)
