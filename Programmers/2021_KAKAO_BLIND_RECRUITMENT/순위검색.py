# 순위검색
'''
def solution(info, query):
    answer = []
    info = [i.split() for i in info]
    query = [q.replace('and', '').split() for q in query]
    for q in query:
        cnt = 0
        for one_info in info:
            chk = False
            for i in range(4):
                if q[i] == '-':
                    continue
                if one_info[i] != q[i]:
                    chk = True
                    break
            if chk:
                continue
            if int(one_info[-1]) >= int(q[-1]):
                cnt += 1
        answer.append(cnt)

    return answer
정확성 18/18
효율성 0/4
'''
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = {}
    info = [i.split() for i in info]
    query = [q.replace('and', '').split() for q in query]
    for one_info in info:
        info_key = one_info[:-1]
        info_value = one_info[-1]
        for i in range(5):
            for c in combinations(info_key, i):
                tmp = ''.join(c)
                if info_dict.get(tmp):
                    info_dict[tmp].append(int(info_value))
                else:
                    info_dict[tmp] = [int(info_value)]

    for k in info_dict.keys():
        info_dict[k].sort()

    for q in query:
        temp = info_dict.get(''.join(q[:-1]).replace('-', ''))
        if not temp:
            answer.append(0)
            continue
        length = len(temp)
        cnt = bisect_left(temp, int(q[-1]))
        answer.append(length - cnt)

    return answer


print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]))
# [1,1,1,1,2,4]
