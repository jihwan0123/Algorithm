# 5347. LCM

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]


def gcd(x, y):  # 최대공약수
    if x == 1:
        return 1
    if x % y == 0:
        return y
    return gcd(y, x % y)


for num in nums:
    a = max(num)
    b = min(num)
    c = gcd(a, b)
    print((a*b)//c)
