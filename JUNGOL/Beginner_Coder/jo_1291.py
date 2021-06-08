# 1291. 구구단

while True:
    s, e = map(int, input().split())
    if 2<= s <= 9 and 2<= e <= 9:
        break
    print("INPUT ERROR!")

if s >= e:
    for j in range(1, 10):
        for i in range(s,e-1, -1):
            print(f'{i} * {j} = {i*j:2d}',end='   ')
        print()
else: # s < e
    for j in range(1, 10):
        for i in range(s,e+1):
            print(f'{i} * {j} = {i*j:2d}', end='   ')
        print()
