# 4673. 셀프 넘버

visited = [0] * 10001

for num in range(1, 10001):
    num = num + sum(list(map(int, str(num))))
    if num < 10001:
        visited[num] = 1

for n in range(1, 10001):
    if not visited[n]:
        print(n)
