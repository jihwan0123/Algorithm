# 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, 
# T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 

places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], 
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]

diag = [[1,1],[-1,-1],[1,-1],[-1,1]]
dxy = [[0,1],[1,0],[-1,0],[0,-1]]
dxy2 = [[0,2],[2,0],[-2,0],[0,-2]]

def check(p):
    for x in range(5):
        for y in range(5):
            if p[x][y] == 'P':
                for dx, dy in dxy:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5 and p[nx][ny] == 'P':
                        return 0
                for dx, dy in dxy2:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5 and p[nx][ny] == 'P':
                        if p[x + dx//2][ny] == 'O' or p[nx][y+dy//2] == 'O':
                            return 0

                for dx, dy in diag:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5 and p[nx][ny] == 'P':
                        if p[x][ny] == 'O' or p[nx][y] == 'O':
                            return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer

print(solution(places))