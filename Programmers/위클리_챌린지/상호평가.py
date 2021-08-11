def grade(s):
    if s >= 90:
        return "A"
    elif s >= 80:
        return "B"
    elif s >= 70:
        return "C"
    elif s >= 50:
        return "D"
    return "F"
    
def solution(scores):
    answer = ''
    n = len(scores)
    scores = list(zip(*scores))
    totals = [[sum(scores[i]), n] for i in range(n)]
    for i in range(n):
        maxV = max(scores[i])
        minV = min(scores[i])
        if ((maxV == scores[i][i]) and (scores[i].count(maxV) == 1)) \
            or ((minV == scores[i][i] and scores[i].count(minV) == 1)):
            totals[i][0] -= scores[i][i]
            totals[i][1] -= 1
    
    for j in range(n):
        answer += (grade(totals[j][0]/totals[j][1]))

    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))