# 1175: 주사위 던지기2

n, m = map(int, input().split())

res = [0] * n


def dice(lev, total):
    if lev == n and total == m:
        print(*res)
        return

    for i in range(1, 7):
        if total + i <= m and lev + 1 <= n and total + i + 6 * (n-lev-1) >= m:
            res[lev] = i
            dice(lev + 1, total + i)
            res[lev] = 0


dice(0, 0)
