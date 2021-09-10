# [3차] 방금그곡

# C#, D#, F#, G#, A#
def solution(m, musicinfos):
    answer = []
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    for musicinfo in musicinfos:
        musicinfo = musicinfo.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        start, end, title, music = musicinfo.split(',')
        start_hour, start_min = map(int, start.split(':'))
        end_hour, end_min = map(int, end.split(':'))
        total_min = 60 * (end_hour - start_hour) + (end_min - start_min)
        temp = music * (int(total_min/len(music))+1)
        temp = temp[:total_min]
        if m in temp:
            answer.append((title, total_min))
    
    if answer:
        answer = sorted(answer, key=lambda x: (-x[1]))[0][0]
    else:
        answer = "(None)"

    return answer

print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))