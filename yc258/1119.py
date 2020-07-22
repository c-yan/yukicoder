X, Y, Z = map(int, open(0).read().split())

if X % 3 == 0 or Y % 3 == 0 or Z % 3 == 0:
    print('Yes')
else:
    print('No')
