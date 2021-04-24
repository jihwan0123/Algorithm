# 17071. 숨바꼭질5

N, K = map(int, input().split())
# N : 수빈, K : 동생

def bfs(idx, a, b):
    global ans
    if b > 500000:
        ans = -1
        return
    if a == b:
        ans = idx
        return

    elif a > b:
        if a % 2:
            a -= 1
        else:
            a += 1
    else:
        a = a * 2
    idx += 1
    bfs(idx, a, b+idx)

ans = 0
bfs(0,N,K)
print(ans)