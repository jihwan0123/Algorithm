# 최소직사각형

def solution(sizes):
    if len(sizes) == 1:
        return sizes[0][0] * sizes[0][1]
        
    temp = []
    for size in sizes:
        temp.append((max(size), min(size)))
    
    a = sorted(temp, key=lambda x:(-x[0], x[1]))
    x = a[0]
    temp.remove(x)
    b = sorted(temp, key=lambda x:(-x[1]))
        
    return a[0][0] * b[0][1]