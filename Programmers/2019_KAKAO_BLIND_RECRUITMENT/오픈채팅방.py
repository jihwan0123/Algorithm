# 오픈채팅방

# Enter, Leave, Change
def solution(record):
    answer = []
    user = {}
    # Enter / Change: 들어오거나 닉네임 변경했을 때 id의 닉네임을 저장
    for i in record:
        items = i.split()
        if items[0] == 'Enter' or items[0] == 'Change':
            user[items[1]] = items[2] # user_id : username
            
    # Enter / Leave: 나갔을 때 채팅 출력
    for i in record:
        items = i.split()
        if items[0] == 'Enter':
            answer.append(user[items[1]] + '님이 들어왔습니다.')
        elif items[0] == 'Leave':
            answer.append(user[items[1]] + '님이 나갔습니다.')
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))