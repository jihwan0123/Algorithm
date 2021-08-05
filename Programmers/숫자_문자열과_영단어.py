words = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
def solution(s):
    i = 0
    while i < len(s):
        if words.get(s[i:i+5]):
            s = s[:i] + words.get(s[i:i+5]) + s[i+5:]
        if words.get(s[i:i+4]):
            s = s[:i] + words.get(s[i:i+4]) + s[i+4:]
        if words.get(s[i:i+3]):
            s = s[:i] + words.get(s[i:i+3]) + s[i+3:]
        i += 1
    answer = int(s)
    return answer