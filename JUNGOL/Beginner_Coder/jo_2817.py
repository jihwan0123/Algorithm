# 2817: 로또(lotto)

data = list(map(int, input().split()))
n = data[0]
s = data[1:]
result = [0] * n


def lotto(start, lev):
    if lev >= 6:
        print(*result[:6])
        return

    for i in range(start, n):
        if s[i] not in result:
            result[lev] = s[i]
            lotto(i, lev+1)
            result[lev] = 0


lotto(0, 0)
