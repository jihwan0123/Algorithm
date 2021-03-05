a = input().split()
P = int(a[0])
K = int(a[1])

if P >= K:
    print(P - K + 1)
else:
    print(999 - K + 1 + P)