# 1856: 숫자사각형2

n, m = map(int,input().split())
cnt = 1
for i in range(n):
    width = []
    for j in range(m):
        width.append(f'{cnt} ')
        cnt += 1
    if i % 2:
        print(''.join(reversed(width)))
    else:
        print(''.join(width))