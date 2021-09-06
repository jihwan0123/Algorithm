# 뉴스 클러스터링

def solution(str1, str2):
    str1_list = []
    str2_list = []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_list.append(str1[i:i+2].upper())
            
    for j in range(len(str2)-1):
        if str2[j:j+2].isalpha():
            str2_list.append(str2[j:j+2].upper())

    # 둘 다 공집합이면 J(A,B) = 1
    if not str1_list and not str2_list:
        return 65536

    # 합집합
    union = set(str1_list).union(set(str2_list))
    length1 = len(union)
    for i in union:
        x1 = str1_list.count(i)
        x2 = str2_list.count(i)
        if x1 > 1 or x2 > 1:
            if x1 > x2:
                length1 += x1-1
            else:
                length1 += x2-1

    # 교집합
    intersection = []
    str1_copy = str1_list.copy()
    for j in str2_list:
        if j in str1_copy:
            intersection.append(j)
            str1_copy.remove(j)

    length2 = len(intersection)

    return int(length2/length1 * 65536)


print(solution("FRANCE", 'french'))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))