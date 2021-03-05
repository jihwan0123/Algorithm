T = int(input()) # test case 갯수

for i in range(1, T + 1):
    tc = input()
    num = list(map(int,tc.split()))
    if num[0] > num[1]:
        print(f'#{i} >')
    elif num[0] == num[1]:
        print(f'#{i} =')
    else:
        print(f'#{i} <')
