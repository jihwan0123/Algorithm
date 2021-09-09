# [3차] 파일명 정렬

def solution(files):
    answer = []
    for file in files:
        temp = []
        number = ''
        first = True
        for i in range(len(file)):
            if file[i].isdigit():  # 숫자면 다음꺼 확인
                number += file[i]
                if first:
                    temp.append(file[:i]) # head
                    first = False
                    continue
            elif (len(temp) == 1) and (first == False): # 숫자가 아니고 head를 저장했으면 number, tail 저장
                temp.append(number) # number
                temp.append(file[i:]) # tail
                number = ''
                break
        if number: # number 뒤에 아무것도 없을경우 런타임에러 발생
            temp.append(number)
        answer.append(temp)

    answer = sorted(answer, key=lambda x: (x[0].upper(), int(x[1])))
    return [''.join(a) for a in answer]


print(solution(["img12.png", "img10.png", "img02.png","img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
