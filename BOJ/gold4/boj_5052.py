# 5052. 전화번호 목록

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    numbers = dict()
    for _ in range(n):
        phone = input().strip()
        numbers[phone] = 1
    ans = "YES"
    for number in numbers:
        temp = ""
        for x in number:
            temp += x
            if numbers.get(temp, 0) and temp != number:
                ans = "NO"
                break
        if ans == "NO":
            break
    print(ans)
