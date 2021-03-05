T = int(input())  # test case 갯수

for i in range(1, T + 1):
    tc = input()
    num = list(map(int, tc.split()))
    print(f'#{i} {max(num)}')
