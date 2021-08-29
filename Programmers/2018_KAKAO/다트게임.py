# 다트게임

def solution(dartResult):
    dartResult = dartResult.replace("10","X")
    score = [0,0,0]
    n = 0
    for i in dartResult:
        if i.isdigit():
            score[n] = int(i)
            n += 1
        elif i == 'X':
            score[n] = 10
            n += 1
        elif i == 'D':
            score[n-1] = score[n-1]**2
        elif i == 'T':
            score[n-1] = score[n-1]**3
        elif i == '*':
            if n>=2:
                score[n-1] *= 2
                score[n-2] *= 2
            else:
                score[n-1] *= 2
        elif i == '#':
            score[n-1] *= -1
        else:
            continue

            
    return sum(score)

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))