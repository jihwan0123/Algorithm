# 문자열 압축

def solution(s):
    length = len(s)
    answer = length
    
    for d in range(1,length):
        words = [s[i:i+d] for i in range(0, length, d)]
        cnt = 1
        after_word = ""
        
        for j in range(1, len(words)):
            x = words[j-1]
            y = words[j]
            if x == y:
                cnt += 1
            else:
                if cnt > 1:
                    after_word += (str(cnt) + x)
                else:
                    after_word += x
                cnt = 1
                
        if cnt > 1:
            after_word += (str(cnt) + y)
        else:
            after_word += y

        answer = min(answer, len(after_word))
            
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))