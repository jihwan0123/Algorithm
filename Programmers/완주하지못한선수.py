from collections import Counter

def solution(participant, completion):
    answer = ''
    a = Counter(participant)
    b = Counter(completion)
    for i in a:
        if a.get(i) != b.get(i):
            answer = i
    return answer