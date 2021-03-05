# 1224. 계산기3

import sys

sys.stdin = open('swea_1224.txt')

# in-stack priority
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
# in-coming priority
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
# lambda 표현식 dict
calc = {"+": (lambda a, b: a + b),
        "-": (lambda a, b: a - b),
        "*": (lambda a, b: a * b),
        "/": (lambda a, b: a / b)
        }


# 중위 -> 후위
def postfix(calc_list):
    op = []  # 연산자 임시 저장
    result = []  # 후위연산으로 바꾼 결과 저장
    for i in calc_list:
        # 숫자면
        if i.isdigit():
            # 그대로 스택에 저장
            result.append(i)

        # 연산자면
        else:
            # 여는 괄호면 무조건 op에 추가
            if i == '(':
                op.append(i)

            # 닫는 괄호면
            elif i == ')':
                for _ in range(len(op)):
                    # 여는 괄호가 나오면 여는괄호 pop해서 없애고 종료
                    if op[-1] == '(':
                        op.pop()
                        break
                    # 여는괄호 나올때까지 pop
                    else:
                        result.append(op.pop())

            # 괄호가 아닌 연산자면
            else:
                # 연산자 스택 비었으면 추가
                if not op:
                    op.append(i)

                # op에 들어있는 연산자와 우선 순위 비교
                else:
                    # 현재 연산자가 op에 들어있는 연산자보다 우선순위가 높으면 추가
                    if isp[i] > isp[op[-1]]:
                        op.append(i)

                    # op에 있는 연산자가 현재 연산자와 같거나 크면
                    # op의 연산자를 빼서 result에 추가하고, op에 현재 연산자 추가
                    else:
                        result.append(op.pop())
                        op.append(i)
    # stack에 남아있는 연산자 추가
    while op:
        result.append(op.pop())

    return result


def calculation(data):
    stack = []
    for x in data:
        if x.isdigit():
            stack.append(int(x))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(calc[x](a, b))

    return stack[0]


for tc in range(1, 11):
    N = int(input())
    problem = input()
    res = calculation(postfix(problem))
    print('#{} {}'.format(tc, res))
