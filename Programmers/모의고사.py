# 완전탐색 - 모의고사

person1 = [1,2,3,4,5]
person2 = [2,1,2,3,2,4,2,5]
person3 = [3,3,1,1,2,2,4,4,5,5]

def solution(answers):
    answer = []
    x = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == person1[i%5]:
            x[0] += 1
        if answers[i] == person2[i%8]:
            x[1] += 1
        if answers[i] == person3[i%10]:
            x[2] += 1
    
    for idx, value in enumerate(x,1):
        if value == max(x):
            answer.append(idx)
            
    return answer