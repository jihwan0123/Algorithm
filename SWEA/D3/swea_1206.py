# 1206. View

import sys

sys.stdin = open('input_view.txt')

T = 10

for tc in range(1, T + 1):
    length = int(input())
    buildings = list(map(int, input().split()))
    # print(buildings)
    count = 0
    for i in range(2, len(buildings) - 2):
        if buildings[i] > buildings[i - 1] and buildings[i] > buildings[i - 2] and buildings[i] > buildings[i + 1] and \
                buildings[i] > buildings[i + 2]:
            count_list = []
            view = abs(buildings[i] - buildings[i - 1])
            count_list.append(abs(buildings[i] - buildings[i - 1]))
            count_list.append(abs(buildings[i] - buildings[i - 2]))
            count_list.append(abs(buildings[i] - buildings[i + 1]))
            count_list.append(abs(buildings[i] - buildings[i + 2]))
            for j in count_list:
                if view > j:
                    view = j
            count += view
    print('#%d %d' % (tc, count))
