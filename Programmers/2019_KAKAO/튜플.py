# 튜플

def solution(s):
    answer = []
    s_list = []
    temp = []
    t = ''
    for i in s[1:-1]:
        if i.isdigit():
            t += i
        else:
            if t:
                temp.append(int(t))
                t = ''
            if i == '}':
                s_list.append(temp)
                temp = temp.copy()
                temp.clear()

    sorted_list = sorted(s_list, key=lambda x: len(x))
    for x in sorted_list:
        for y in x:
            if y not in answer:
                answer.append(y)

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))  # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))  # [2, 1, 3, 4]
print(solution("{{20,111},{111}}"))  # [111,20]
print(solution("{{123}}"))  # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))  # [3, 2, 4, 1]
