# 4047 영준이의 카드카운팅

import sys

sys.stdin = open('swea_4047.txt')

for tc in range(1, int(input()) + 1):
    S = input()
    # TXY * 4
    # T : 카드무늬(S D H C)
    # XY : 01 ~ 13

    br = False
    card = {}
    card['S'] = []
    card['D'] = []
    card['H'] = []
    card['C'] = []
    for i in range(0, len(S), 3):  # 0, 3, 6, 9
        t, xy = S[i:i + 1], int(S[i + 1:i + 3])
        if xy in card[t]:
            br = True
            break
        else:
            card[t].append(xy)
            # print(card)

    if br:
        print('#{}'.format(tc), 'ERROR')
        continue

    print('#{}'.format(tc), end=' ')
    print(str(13 - len(card['S'])) + ' ' + str(13 - len(card['D'])) + ' ' + str(13 - len(card['H']))
          + ' ' + str(13 - len(card['C'])))

####### 처음 코드 ##########

# for tc in range(1, int(input()) + 1):
#     S = input()
#     # TXY * 4
#     # T : 카드무늬(S D H C)
#     # XY : 01 ~ 13
#     S_list = [i for i in range(1, 14)]
#     D_list = [i for i in range(1, 14)]
#     H_list = [i for i in range(1, 14)]
#     C_list = [i for i in range(1, 14)]
#     br = False
#     s, d, h, c = 13, 13, 13, 13
#
#     for i in range(0, len(S), 3):  # 0, 3, 6, 9
#         t, xy = S[i:i + 1], int(S[i + 1:i + 3])
#         if t == 'S' and xy in S_list:
#             S_list.remove(xy)
#             s -= 1
#         elif t == 'D' and xy in D_list:
#             D_list.remove(xy)
#             d -= 1
#         elif t == 'H' and xy in H_list:
#             H_list.remove(xy)
#             h -= 1
#
#         elif t == 'C' and xy in C_list:
#             C_list.remove(xy)
#             c -= 1
#         else:
#             print('#{}'.format(tc), 'ERROR')
#             br = True
#             break
#
#     if br:
#         continue
#
#     print('#{} {} {} {} {}'.format(tc, s, d, h, c))


##### 제일 짧은 코드 #########

# for t in range(1,int(input())+1):
#     s=input();c={'S':13,'D':13,'H':13,'C':13}
#     for i in range(0,len(s),3):
#         c[s[i]]-=1
#         if s.count(s[i:i+3])>1:c={0:'ERROR'};break
#     print('#%i'%t,*c.values())
