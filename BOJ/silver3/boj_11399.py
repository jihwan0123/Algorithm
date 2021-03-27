# 11399. ATM

def bubble_sort():
    for i in range(n-1):
        for j in range(i, n):
            if times[i] > times[j]:
                times[i], times[j] = times[j], times[i]

T = int(input())

times = list(map(int,input().split()))
n = len(times)
bubble_sort()
for i in range(1, n):
    times[i] += times[i-1]


print(sum(times))