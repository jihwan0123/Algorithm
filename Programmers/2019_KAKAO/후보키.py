# 후보키

from itertools import chain, combinations

# 유일성 만족하는 집합
def get_uniqueness(relation):
    length = len(relation[0])
    nums = list(range(length))
    # 컬럼으로 만들 수 있는 전체 조합
    combi_list = chain.from_iterable(combinations(nums,r) for r in range(length + 1))
    unique_list = []
    for combi in combi_list:
        unique = True
        row_list = dict()
        # 유일성 만족하는지 체크
        for i in range(len(relation)):
            row = ''
            for j in combi:
                row += relation[i][j]
            # 2개이상 존재하면 유일성 X
            if row_list.get(row):
                unique = False
                break
            row_list[row] = 1
        # 유일성 만족하면 추가
        if unique:
            unique_list.append(combi)
    return unique_list

def solution(relation):
    unique_list = get_uniqueness(relation)
    answer = []
    # 최소성 만족하는지 체크
    for combi in unique_list:
        c = set(combi)
        check = True
        for i in answer:
            # answer중에서 combi의 subset이 존재하면, 최소성을 만족하지 않는다.
            if i.issubset(combi):
                check = False
                break
        if check:
            answer.append(c)

    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
