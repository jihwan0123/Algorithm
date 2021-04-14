# 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔


import sys

sys.stdin = open('sample_input.txt')

password = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}


def check_code(arr):
    check = (arr[0] + arr[2] + arr[4] + arr[6]) * 3 + (arr[1] + arr[3] + arr[5]) + arr[7]
    if check % 10:
        return 0
    else:
        return sum(arr)


def get_one_code(arr, cnt):
    nbits = cnt * 7
    n_length = nbits << 3
    temp = arr[-n_length:]
    c = []
    for i in range(0, len(temp), nbits):
        num = password.get(temp[i:i + nbits][::cnt], 'X')
        if num == 'X':
            return 0
        c.append(num)
    return c


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    data = set(input()[:M] for _ in range(N))
    code = []
    ans = 0

    for i in data:
        if i.count('0') != M:
            code.append(bin(int(i, 16))[2:].rstrip('0'))

    result = []

    for j in code:
        c_list = []
        while j:
            k = 1
            while True:
                j = j.zfill(k * 56)
                x = get_one_code(j, k)
                if x != 0:
                    c_list.append(x)
                    n_bits = (k * 7) << 3
                    j = j[:len(j) - n_bits].rstrip('0')
                    break
                k += 1
        for i in c_list:
            if i and i not in result:
                result.append(i)
                ans += check_code(i)

    print('#%d %d' % (tc, ans))
