# 2588. 곱셈

num1 = int(input())
num2 = input()

for n in range(len(num2)-1,-1,-1):
    print(num1 * int(num2[n]))

print(num1 * int(num2))