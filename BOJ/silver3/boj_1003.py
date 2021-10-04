# 1003. 피보나치 함수

t = int(input())
fib = [[0] * 41 for _ in range(2)]
fib[0][0] = 1
fib[1][1] = 1

for i in range(2, 41):
    fib[0][i] = fib[0][i-1] + fib[0][i-2]
    fib[1][i] = fib[1][i-1] + fib[1][i-2]

for _ in range(t):
    n = int(input())
    print(fib[0][n], fib[1][n])