for i in range(0, 5):
    result = [0,0,0,0,0]
    for j in range(0, 5):
        result[i] = '#'
        result[j] = '+'
    print(''.join(result))