# 9663. N Queen
# 0 < n <= 15
n = int(input())


def isPossible(col):
    for i in range(col):
        # 같은 열, 대각선인지 검사
        if check[col] == check[i] or abs(col-i) == abs(check[col]-check[i]):
            return False

    return True


def nQueen(idx):
    global cnt
    # n개를 다 놨으면 count
    if idx == n:
        cnt += 1
        return

    # 0 ~ n-1까지 반복하면서 가능한지 검사
    for i in range(n):
        check[idx] = i
        if isPossible(idx):
            nQueen(idx+1)


cnt = 0
check = [0] * n
nQueen(0)
print(cnt)
