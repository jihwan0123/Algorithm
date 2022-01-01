# 24039. 2021은 무엇이 특별할까?

import sys

input = sys.stdin.readline

n = int(input())
MAX = 105
nums = list(range(MAX))

for i in range(2, int(MAX ** 0.5) + 1):
    if nums[i]:
        for j in range(i * 2, MAX, i):
            nums[j] = 0

prime_numbers = []
for i in range(2, MAX):
    if nums[i]:
        prime_numbers.append(i)

nums = []
for i in range(1, len(prime_numbers)):
    if prime_numbers[i] * prime_numbers[i - 1] > n:
        print(prime_numbers[i] * prime_numbers[i - 1])
        break
