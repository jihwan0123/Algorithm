# 12904. A 와 B

'''
# 시간초과 발생
S = input()
T = input()

queue = [S]
ans = 0

while queue:
    n = queue.pop()
    if n == T:
        ans = 1
        break

    n1 = n + 'A'
    n2 = n[::-1] + 'B'

    if len(n1) <= len(T):
        queue.append(n1)

    if len(n2) <= len(T):
        queue.append(n2)

print(ans)
'''

# 거꾸로 긴거부터 시작
S = list(input())
T = list(input())

while len(S) < len(T):
    if T[-1] == 'A':
        T.pop()
    
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1]
    

if S == T:
    print(1)
else:
    print(0)


