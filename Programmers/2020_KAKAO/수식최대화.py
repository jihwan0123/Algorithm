# 수식최대화

from itertools import permutations
import re

calc = {
        "+": (lambda a, b: a + b),
        "-": (lambda a, b: a - b),
        "*": (lambda a, b: a * b)
    }


def solution(expression):
    answer = 0
    operations = list(permutations(['*', '+', '-'], 3))
    expression = re.split(r'(\D)',expression)
    for oper in operations:
        temp = expression.copy()
        for i in range(3):
            while oper[i] in temp:
                idx = temp.index(oper[i])
                a = int(temp.pop(idx-1))
                op = temp.pop(idx-1)
                b = int(temp.pop(idx-1))
                temp.insert(idx-1, calc[op](a,b))
        answer = max(answer, abs(temp[0]))
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
