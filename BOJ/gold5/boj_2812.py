# 2812. 크게 만들기

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
num = deque(map(int, input().strip()))
stack = []

cnt = 0
chk = False 

while cnt < k: # k개 제거하면 종료
    if stack and num[0] > stack[-1]: # stack 마지막 값보다 넣으려는 값이 더 크면
        stack.pop() # pop하고
        cnt += 1 # 제거한 횟수 +1 하고 현재 stack에 있는 앞에값보다 큰지 확인
        continue

    # num 맨 앞의 값 stack에 저장
    temp = num.popleft()
    stack.append(temp)

    # 종료조건, 전체 길이가 n-k만큼 쌓였고, 
    # num에 남은 최대값보다 stack의 마지막값이 크거나 같으면
    if len(stack) >= n-k and max(num) <= stack[-1]:
        # 그대로 출력하면 되는지 표시
        chk = True
        break

if chk:
    print(''.join(map(str, stack)))
else: # n-k개 stack에 넣기 전에 k개 제거했으면 stack에 넣은 값과 뒤에 남은값 더해서 출력
    print(''.join(map(str, stack + list(num))))
