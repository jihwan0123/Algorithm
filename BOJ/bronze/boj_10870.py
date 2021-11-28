# 10870. 피보나치 수 5
import sys
input = sys.stdin.readline

n = int(input())
fibo = [0] * 21
fibo[1] = fibo[2] = 1

for i in range(3, n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[n])
