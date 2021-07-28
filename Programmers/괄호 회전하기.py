bracket = {
    ']' : '[',
    ')' : '(',
    '}' : '{'
}
def check(a):
    stack = []

    for i in a:
        if i == '(' or i =='{' or i=='[':
            stack.append(i)
        elif i == '}' or i == ')' or i == ']':
            if len(stack) == 0 or stack[len(stack)-1] != bracket[i]:
                return 0
            stack.pop()

    if len(stack) != 0:
        return 0
    else:
        return 1

def solution(s):
    answer = 0
    x = len(s)
    z = list(s)
    while x:
        x -= 1
        a = z.pop(0)
        z.append(a)
        if check(z):
            answer += 1

    return answer