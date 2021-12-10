# 15927. 회문은 회문아니야!!

import sys
input = sys.stdin.readline

string = input().rstrip()

# 모든 문자열이 같으면 -1
if string[0] * len(string) == string:
    print(-1)
    sys.exit()

s = 0
e = len(string)-1

# 전체가 회문인지 체크
while s < e:
    # 회문이 아니면 전체 길이
    if string[s] != string[e]:
        print(len(string))
        sys.exit()
    s += 1
    e -= 1

# 회문이면, 앞이나 뒤에서 1개 뺀 길이
print(len(string)-1)
