# N-Queen

def dfs(queen, row, n):
    global answer
    if n == row:
        answer += 1
        return
    for col in range(n):
        # row번째 열에 n까지 Queen을 놔본다.
        queen[row] = col
        for i in range(row):
            # 앞에 놨던 Queen과 같은 열이나, 대각선에 놓여져 있으면 종료
            if queen[i] == queen[row] or abs(queen[i] - queen[row]) == row - i: 
                break
        # 다음 row에 놔보러 이동
        else:
            dfs(queen, row + 1, n)

def solution(n):
    global answer
    answer = 0
    queen = [0] * n
    dfs(queen, 0, n)
    return answer


for x in range(1, 12):
    print(solution(x))