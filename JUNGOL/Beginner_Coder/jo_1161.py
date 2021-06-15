# 1161: 하노이1

# 시작, 중간, 도착
def hanoi(n, start, mid, to):
    if n == 0:
        return

    # n-1개를 to를 경유해서 mid로 옮긴다.
    hanoi(n-1, start, to, mid)
    print(f'{n} : {start} -> {to}')
    # 옮긴 mid에 있는 탑을 start를 경유해서 to로 옮긴다.
    hanoi(n-1, mid, start, to)


hanoi(int(input()), 1, 2, 3)
