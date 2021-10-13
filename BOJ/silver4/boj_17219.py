# 17219. 비밀번호 찾기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

addr = {}
for _ in range(n):
    address, password = input().strip().split()
    addr[address] = password

for _ in range(m):
    address = input().strip()
    print(addr.get(address))