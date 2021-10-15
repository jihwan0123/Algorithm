def solution(line):
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = -float('inf'), -float('inf')
    answer = []
    stars = []

    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a, b, e = line[i][0], line[i][1], line[i][2]
            c, d, f = line[j][0], line[j][1], line[j][2]
            m = a*d - b*c
            if (m == 0): continue
            x = (b*f - e*d)/m
            y = (e*c - a*f)/m
            if (x != int(x)): continue
            if (y != int(y)): continue
            x = int(x)
            y = int(y)
            min_x, min_y = min(min_x, x), min(min_y, y)
            max_x, max_y = max(max_x, x), max(max_y, y)
            stars.append((x, y))

    for i in range(max_y, min_y-1, -1):
        temp = ''
        for j in range(min_x, max_x+1):
            if (j, i) in stars:
                temp += '*'
            else:
                temp += '.'
        answer.append(temp)

    return answer


print(solution([[2, -1, 4], [-2, -1, 4],[0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))