# 1341. 구구단2


while True:
    s, e = map(int, input().split())
    if 2<= s <= 9 and 2<= e <= 9:
        break
    print("INPUT ERROR!")

if s >= e:
    for i in range(s,e-1, -1):
        for j in range(1, 10):
            print(f'{i} * {j} = {i*j:2d}',end='   ')
            if j % 3 == 0:
                print()
        print()
else:
    for i in range(s,e+1):
        for j in range(1, 10):
            print(f'{i} * {j} = {i*j:2d}', end='   ')
            if j % 3 == 0:
                print()
        print()
