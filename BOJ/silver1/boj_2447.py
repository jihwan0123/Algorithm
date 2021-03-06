# 2447. 별찍기 -10

### 전체를 다 돌면서 별을 찍어서 시간이 오래걸리는것 같다.

# 9등분으로 나눠서
# 1 2 3
# 4 5 6
# 7 8 9
# 5번에 해당하는 부분이 공백이므로 별 찍지않고 넘어간다.


def star(x, y, n):
    # 크기 1이면 종료
    if n == 1:
        point[x][y] = '*'
        return

    m = n // 3

    # 크게 9개의 구역으로 나눈다.
    for i in range(3):
        for j in range(3):
            # i, j = 1일때 위에서 5번 부분이므로 건너뜀
            if i != 1 or j != 1:
                star(x + i * m, y + j * m, m)


N = int(input())
point = [[' '] * N for _ in range(N)]

star(0, 0, N)

for r in point:
    print(''.join(r))

'''
##### 한번에 합치는 코드 #####
# boj - wider93님 풀이

def concatenate(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)]
 
def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    a = concatenate(x, x)
    b = concatenate(x, [' '*n]*n)
 
    return a + b + a
 
print('\n'.join(star10(int(input()))))

'''
