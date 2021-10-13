# 17626. Four Squres

def chk(n):
    temp = int(n**0.5)
    # 제곱인 경우 체크 (1인 경우)
    i = temp
    while i:
        if i**2 == n:
            return 1
        i -= 1

    # 제곱인거 빼고 제곱수로 되는지 체크 (2인 경우)
    i = temp
    while i:
        n2 = n - i**2
        if n2 == int(n2**0.5) ** 2:
            return 2
        i -= 1

    # 3인경우 체크
    for i in range(1, 224):
        for j in range(i, 224):
            # 제곱수 2개 뺀값
            n3 = n - i**2 - j**2
            if n3 < 0: break
            if n3 == int(n3**0.5) ** 2:
                return 3

    # 최댓값이 4이므로 4
    return 4


n = int(input())
ans = chk(n)
print(ans)
