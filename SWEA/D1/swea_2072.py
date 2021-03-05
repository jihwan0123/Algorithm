test_num = int(input())
for i in range(test_num):
    num = list(map(int, input().split()))
    total = 0
    for j in num:
        if j % 2 != 0:
            total += j
    print(f'#{i + 1} {total}')
