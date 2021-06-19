# 2811: 소수와 합성수
import math
def isPrime(number):
    for i in range(2, round(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def check(n):
    if n < 2:
        return 'number one'

    if isPrime(n):
        return 'prime number'
    else:
        return 'composite number'


nums = list(map(int, input().split()))
for num in nums:
    print(check(num))
