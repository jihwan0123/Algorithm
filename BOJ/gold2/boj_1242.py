# 1242. 소풍

n, k, m = map(int, input().split())
# n명, k:말하면 퇴장, m:동호의 번호
start = 0
ans = 1
m -= 1
while True:
    removed = (start + k - 1) % n
    if removed == m:
        break
    if removed < m:
        m -= 1
    # if removed > m:
    #     pass
    start = removed
    n -= 1
    ans += 1

print(ans)