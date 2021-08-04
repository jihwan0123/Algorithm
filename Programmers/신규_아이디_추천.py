# 신규 아이디 추천

# 문자열 메소드 이용
def solution(new_id):
    answer = ''
    new_id = new_id.lower()  # 1단계
    for c in new_id:  # 2단계
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c

    while '..' in answer:  # 3단계
        answer = answer.replace('..', '.')

    if answer[0] == '.':  # 4단계
        if len(answer) > 1:
            answer = answer[1:]
        else:
            answer = '.'  # 안해주면 index error 발생

    if answer[-1] == '.':
        answer = answer[:-1]

    if answer == '':  # 5단계
        answer = 'a'
    if len(answer) >= 16:  # 6단계
        answer = answer[:15].rstrip('.')

    if len(answer) == 2:
        answer = answer[:1] + answer[-1] + answer[-1]
    elif len(answer) == 1:
        answer = answer*3

    return answer


# 정규식 사용
'''
import re

def solution(new_id):
    answer = ''
    new_id = new_id.lower() # 1단계
    new_id = re.sub('[^a-z\d\-\_\.]', '', new_id) # 2단계
    new_id = re.sub("\.\.+", ".", new_id) # 3단계
    new_id = re.sub('^\.|\.$', '', new_id) # 4단계
    if new_id == '': # 5단계
        new_id = 'a'
    if len(new_id) >= 16: # 6단계
        new_id = new_id[:15].rstrip('.')
        
    if len(new_id) == 2:
        new_id = new_id[:1] + new_id[-1] + new_id[-1]
    elif len(new_id) == 1:
        new_id = new_id*3
    
    answer = new_id
    return answer
'''


a = solution("...!@BaT#*..y.abcdefghijklm")
b = solution("z-+.^.")
c = solution("=.=")
d = solution("123_.def")
e = solution("abcdefghijklmn.p")

if a == "bat.y.abcdefghi":
    print(True)
else:
    print(False)

if b == "z--":
    print(True)
else:
    print(False)

if c == "aaa":
    print(True)
else:
    print(False)

if d == "123_.def":
    print(True)
else:
    print(False)

if e == "abcdefghijklmn":
    print(True)
else:
    print(False)
