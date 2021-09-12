# 2138. 전구와 스위치

import sys
input = sys.stdin.readline

def change(x, input_list):
    if x == 0:
        input_list[0] = abs(input_list[0]-1)
        input_list[1] = abs(input_list[1]-1)
    elif x == n-1:
        input_list[-1] = abs(input_list[-1]-1)
        input_list[-2] = abs(input_list[-2]-1)
    else:
        input_list[x-1] = abs(input_list[x-1]-1)
        input_list[x] = abs(input_list[x]-1)
        input_list[x+1] = abs(input_list[x+1]-1)

n = int(input())
first = list(map(int,input().strip('\n')))
last = list(map(int,input().strip('\n')))

if first == last:
    print(0)
    sys.exit()

# 첫번째 스위치 누르는 경우
temp = first.copy()
change(0, temp)
ans = 1
# 눌렀을때 같으면 바로 종료
if temp == last:
    print(ans)
    sys.exit()
# 다르면 1번 스위치부터 n-1번 스위치까지 돌면서 앞의 전구가 다른경우에 누른다.
for i in range(1, n):
    if temp[i-1] != last[i-1]:
        ans += 1
        change(i, temp)

# 같으면 ans 출력 다르면 안누르는경우로
if temp == last:
    print(ans)
    sys.exit()


# 안누르는 경우 위와 똑같이 반복
ans = 0
for i in range(1, n):
    if first[i-1] != last[i-1]:
        ans += 1
        change(i, first)

if first == last:
    print(ans)
    sys.exit()
else:
    # 마지막까지 다르면 -1
    print(-1)