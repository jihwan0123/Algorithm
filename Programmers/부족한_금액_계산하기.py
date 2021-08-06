# 부족한 금액 계산하기

def solution(price, money, count):
    answer = 0
    for i in range(1,count+1):
        answer += price * i
    if money >= answer:
        answer = 0
    else:
        answer -= money

    return answer