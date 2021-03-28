# 12907. 동물원

N = int(input())
animal = list(map(int,input().split()))
check = [0] * 41
a = 2
res = 1
for i in animal:
    check[i] += 1

for j in check:
    # 2보다 큰게 있으면 불가능
    if j > a:
        res = 0
        break
    # 0이나 1이 나오고 뒤에 큰수가 나와도 불가능
    a = j

# res = 1 이면, 결과값이 존재하므로 계산
if res:
    print(2 ** (check.count(2) + (1 if check.count(1) else 0)))
# 0 이면, 존재하지 않는다.
else:
    print(res)