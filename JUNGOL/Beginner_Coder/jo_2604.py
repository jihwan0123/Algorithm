# 2604: 그릇

bowls = input()
res = 10
for i in range(len(bowls)-1):
    if bowls[i] == bowls[i+1]:
        res += 5
    else: res += 10

print(res)