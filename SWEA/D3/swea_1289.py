# 1289. 원재의 메모리 복구하기

import sys

sys.stdin = open('swea_1289.txt')

for tc in range(1, 1 + int(input())):
    memory = input()
    cnt = 0

    if memory[0] == '1':
        cnt = 1

    for i in range(len(memory) - 1):
        if memory[i] != memory[i + 1]:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
