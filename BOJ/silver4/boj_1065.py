# 1065. 한수

n = int(input())
cnt = 99
if n < 100:
    print(n)
else:
    for i in range(100, n+1):
        temp = list(map(int, str(i)))
        if temp[2] - temp[1] == temp[1] - temp[0]:
            cnt += 1
    print(cnt)