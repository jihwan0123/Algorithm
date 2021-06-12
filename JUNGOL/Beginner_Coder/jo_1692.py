# 1692: 곱셈

a = int(input())
b = int(input())

first = a*(b % 10)
second = a*((b % 100)//10)
third = a*(b//100)

print(first)
print(second)
print(third)
print(first+second*10+third*100)