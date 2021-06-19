# 1009: 각 자리수의 역과 합

cnt = 0
while cnt <= 10:
    res = 0
    rev = ''
    num = int(input())
    if num == 0:
        break
    
    while num:
        x = num % 10
        rev += str(x)
        res += x
        num //= 10
    print(rev.lstrip('0'),res)