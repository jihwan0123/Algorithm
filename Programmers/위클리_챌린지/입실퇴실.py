# 입실 퇴실

def solution(enter, leave):
    answer = [set() for _ in range(len(enter)+1)]
    cur = []
    e, l = 0, 0
    chk = True
    while (e < len(enter)) and (l < len(leave)):
        if chk:
            cur.append(enter[e])
        for c in cur:
            answer[c].add(enter[e])
            answer[enter[e]].add(c)

        if leave[l] in cur:
            cur.remove(leave[l])
            for c in cur:
                answer[leave[l]].add(c)
                answer[c].add(leave[l])
            l += 1
            chk = False
        else:
            chk = True
            e += 1

    return [len(a)-1 for a in answer][1:]

print(solution([1,3,2],[1,2,3]))
print(solution([1,4,2,3],[2,1,3,4]))