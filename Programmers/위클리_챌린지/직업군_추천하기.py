score = {0: 5, 1:4, 2:3, 3:2, 4:1}
def solution(table, languages, preference):
    answer = ''
    ans = {}
    for t in table:
        temp = t.split(' ')
        title = temp[0]
        subjects = temp[1:]
        for i in range(len(subjects)):
            for l in range(len(languages)):
                if languages[l] == subjects[i]:
                    if ans.get(title):
                        ans[title] += score.get(i) * preference[l]
                    else:
                        ans[title] = score.get(i) * preference[l]
    
    answer=sorted(ans.items(),key=lambda x:(-x[1],x[0]))[0][0]
    
    return answer