# 카펫

def solution(brown, yellow):
    answer = []
    x = (brown-4) // 2
    temp = x
    while (x):
        if x * (temp-x) == yellow:
            answer = [x+2, temp-x+2]
            return answer

        x -= 1

    return answer