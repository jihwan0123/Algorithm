# 1523: 별삼각형1

n, m = map(int, input().split())
if n > 100 or not 1 <= m <= 3:
    print('INPUT ERROR!')
else:
    if m == 1:
        stars = [['']*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1):
                stars[i][j] = '*'
        for star in stars:
            if ''.join(star):
                print(''.join(star))

    elif m == 2:
        stars = [['']*n for _ in range(n)]
        for i in range(n):
            for j in range(n-1-i, -1, -1):
                stars[i][j] = '*'
        for star in stars:
            if ''.join(star):
                print(''.join(star))

    elif m == 3:
        stars = [[' ']*(2*n) for _ in range((2*n))]
        for i in range(n):
            for j in range(n-i-1, n+i):
                stars[i][j] = '*'
        for star in stars:
            if ''.join(star).strip():
                print(''.join(star))
