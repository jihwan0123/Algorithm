# 23629. 이 얼마나 끔찍하고 무시무시한 수식이니

import sys
import re
from collections import deque
input = sys.stdin.readline

string_to_num = {
    'ZERO': 0,
    'ONE': 1,
    'TWO': 2,
    'THREE': 3,
    'FOUR': 4,
    'FIVE': 5,
    'SIX': 6,
    'SEVEN': 7,
    'EIGHT': 8,
    'NINE': 9
}
num_to_string = {
    0: 'ZERO',
    1: 'ONE',
    2: 'TWO',
    3: 'THREE',
    4: 'FOUR',
    5: 'FIVE',
    6: 'SIX',
    7: 'SEVEN',
    8: 'EIGHT',
    9: 'NINE'
}
calc = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    'x': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}

string = input().rstrip()[:-1]
# 문자를 숫자로 변환
for n in string_to_num:
    string = string.replace(n, str(string_to_num[n]))

# 연속으로 나오는 연산자 있는지 체크
for i in range(len(string)-1):
    if string[i].isdigit() == False and string[i+1].isdigit() == False:
        print("Madness!")
        sys.exit()

print(string+'=')

# 연산자 저장
queue = deque()
for s in string:
    if s in '+-x/':
        queue.append(s)

# 연산자로 split
nums = deque(re.split('[-,+,x,/]', string))
res = 0
# 연산자 순서대로 계산
while queue:
    op = queue.popleft()
    x = int(nums.popleft())
    y = int(nums.popleft())
    # 음수 나눗셈 예외처리
    if op == '/' and x < 0:
        res = -calc[op](-x, y)
    else:
        res = calc[op](x, y)
    nums.appendleft(res)

res = str(nums[0])
for r in res:
    if r == '-':
        continue
    res = res.replace(r, num_to_string[int(r)])

print(res)
