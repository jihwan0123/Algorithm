# 10912. 외로운 문자

def check(words):
    word = list(words)
    word.sort()  # 'x' 'x' 'y' 'y' 'z' 'z'
    result = []

    for s in word:  # 정렬된 리스트 반복
        if s in result:  # 리스트의 요소가 이미 들어있으면
            result.pop()  # 제거
        else:  # 없으면 자동으로 정렬된 상태로 result에 넣음
            result.append(s)

    if result:
        return result
    else:
        return 'Good'


T = int(input())

for tc in range(1, T + 1):
    words = input()
    result = ''.join(check(words))
    print('#{} {}'.format(tc, result))
