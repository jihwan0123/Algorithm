# 행렬 테두리 회전하기

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def rotate(x1, y1, x2, y2, table):
    ans = []
    x, y = x1, y1
    temp = table[x][y]
    while x < x2:
        nx = x + dxy[0][0]
        ny = y + dxy[0][1]
        table[x][y] = table[nx][ny]
        x = nx
        y = ny
        ans.append(table[x][y])
    while y < y2:
        nx = x + dxy[1][0]
        ny = y + dxy[1][1]
        table[x][y] = table[nx][ny]
        x = nx
        y = ny
        ans.append(table[x][y])
    while x > x1:
        nx = x + dxy[2][0]
        ny = y + dxy[2][1]
        table[x][y] = table[nx][ny]
        x = nx
        y = ny
        ans.append(table[x][y])
    while y > y1:
        nx = x + dxy[3][0]
        ny = y + dxy[3][1]
        table[x][y] = table[nx][ny]
        x = nx
        y = ny
        ans.append(table[x][y])
    table[x1][y1+1] = temp
    ans.append(temp)
    return min(ans)


def solution(rows, columns, queries):
    answer = []
    nums = [[] for _ in range(rows)]
    idx = 0
    for i in range(1, rows*columns+1):
        if i > columns and i % columns == 1:
            idx += 1
        nums[idx].append(i)

    for q in queries:
        x1, y1, x2, y2 = q
        answer.append(rotate(x1-1, y1-1, x2-1, y2-1, nums))
    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97, [[1, 1, 100, 97]]))
