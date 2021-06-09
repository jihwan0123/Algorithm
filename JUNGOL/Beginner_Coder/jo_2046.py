# 2046: 숫자사각형4

n, m = map(int, input().split())
cnt = 1
if m == 1:
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i, end=' ')
        print()

elif m == 2:
    for i in range(n):
        for j in range(n):
            print(cnt, end=' ')
            if i % 2:
                cnt -= 1
            else:
                cnt += 1
        print()
        if i % 2:
            cnt = 1
        else:
            cnt = n


elif m == 3:
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i*j, end=' ')
        print()
