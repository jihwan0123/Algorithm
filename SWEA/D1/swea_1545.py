num = int(input())

for i in range(num, -1, -1):
    if i == 0:
        print(i, end='')
    else:
        print(i, end=' ')
