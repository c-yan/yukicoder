X, Y, Z = map(int, open(0).read().split())

if X * Y * Z % 3 == 0:
    print('Yes')
else:
    print('No')
