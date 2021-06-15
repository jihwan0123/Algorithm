# 1309: 팩토리얼

def factorial(n):
    global total
    if n > 1:
        print(f'{n}! = {n} * {n-1}!')
        total = total * n
        factorial(n-1)
    else:
        print('1! = 1')


total = 1
factorial(int(input()))
print(total)
