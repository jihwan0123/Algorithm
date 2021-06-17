# 1102: 스택(stack)

'''
7
i 7
i 5
c
o
o
o

'''

stack = []


def push(s):
    stack.append(s)
    return


def pop():
    if stack:
        return stack.pop()
    else:
        return 'empty'


n = int(input())
for i in range(n):
    cmd = input()
    if len(cmd) == 1:
        command = cmd
    else:
        command, num = cmd.split()

    if command == 'i':
        push(num)

    elif command == 'c':
        print(len(stack))

    elif command == 'o':
        print(pop())
