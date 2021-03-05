# 테스트 케이스 입력
T = int(input())


for i in range(1, T + 1):
    days = input()
    year = days[0:4]
    month = days[4:6]
    date = days[6:]
    if not 0 < int(month) <= 12:
        print(f'#{i} -1')
    else:
        if int(month) == 2:
            if 0 < int(date) <= 28:
                print(f'#{i} {year}/{month}/{date}')
            else:
                print(f'#{i} -1')
        elif int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7\
             or int(month) == 8 or int(month) == 10 or int(month) == 12:
            if not 0 < int(date) <= 31:
                print(f'#{i} -1')
            else:
                print(f'#{i} {year}/{month}/{date}')
                
        else:
            if not 0< int(date) <= 30:
                print(f'#{i} -1')
            else:
                print(f'#{i} {year}/{month}/{date}')
