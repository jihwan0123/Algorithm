# 메뉴리뉴얼

from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        menu = {}
        for order in orders:
            for combi in combinations(order, c):
                temp = ''.join(sorted(combi))
                if menu.get(temp):
                    menu[temp] += 1
                else:
                    menu[temp] = 1
                
        tmp = max(menu.values())
        if tmp < 2:
            break
        for item, value in sorted(menu.items(), key=lambda item: -item[1]):
            if value == tmp:
                answer.append(item)
            else:
                break
    
    return sorted(answer)





print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))