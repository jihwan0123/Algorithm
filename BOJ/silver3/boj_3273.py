# 3273. 두 수의 합

n = int(input())
a = list(map(int, input().split()))
a.sort()
x = int(input())
l = 0
r = n-1
cnt = 0

while l < r:
    total = a[l] + a[r]
    if total == x:
        cnt += 1
        l += 1
        r -= 1
    elif total < x:
        l += 1
    else:  # total > x
        r -= 1

print(cnt)
