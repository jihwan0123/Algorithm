# 22252. 정보 상인 호석

import sys
import heapq
input = sys.stdin.readline

Q = int(input())  # 쿼리의 갯수
info = {}
price = 0
for _ in range(Q):
    query = input().split()
    name = query[1]
    if query[0] == '1':  # 1이면 고릴라 정보 획득
        if info.get(name):  # 저장되어있으면 건너뛰고 저장
            pass
        else:  # 저장되어 있지 않으면 리스트 만들고 저장
            info[query[1]] = []
        for i in range(3, int(query[2]) + 3):
            heapq.heappush(info[name], -int(query[i]))  # 최대힙 구해야해서 -붙여서 계산

    else:  # 2면 호석이가 정보 구매, 고릴라 정보 파기
        if info.get(name):  # name 이름의 판매자가 있으면
            length = len(info.get(name))  # 길이 체크
            if length >= int(query[2]):  # 현재 들어있는 정보 길이가 더 길면
                for _ in range(int(query[2])):  # 원하는 정보만큼 반복
                    price -= heapq.heappop(info[name])
            else:  # 원하는 정보가 더 많으면 들어있는 정보 전부 다 꺼낸다.
                for _ in range(length):
                    price -= heapq.heappop(info[name])
        else:  # 없으면 다음 쿼리로
            continue

print(price)
