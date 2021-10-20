from collections import Counter

def solution(clothes):
    answer = 1
    cloth = Counter([i[1] for i in clothes])    
    for c in cloth:
        answer *= (cloth[c]+1)
    return answer-1