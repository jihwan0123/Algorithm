t = list(map(int, input().split()))

if t[0] == 1 and t[1] == 2 or t[0] == 2 and t[1] == 3 or t[0] == 3 and t[1] == 1:
    print('B')
elif t[0] == 2 and t[1] == 1 or t[0] == 3 and t[1] == 2 or t[0] == 1 and t[1] == 3:
    print('A')
else:
    print('무승부')
