T = int(input())

for i in range(1, T + 1):
    num = list(map(int,input().split()))
    print(f'{i} {num[0]//num[1]} {num[0]%num[1]}')