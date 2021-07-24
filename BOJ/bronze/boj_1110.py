# 1110. 더하기 사이클
import sys
input = sys.stdin.readline

num = int(input())

ans = [num]
cnt = 0
while True:
    cnt += 1
    if num < 10:
        num = int(str(num) + str(num))
        if num not in ans:
            ans.append(num)
        else:
            print(cnt)
            break
    
    else:
        num = int(str(num%10) + str(num//10 + num%10)[-1])
        if num not in ans:
            ans.append(num)
        else:
            print(cnt)
            break