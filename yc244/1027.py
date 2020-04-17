D1, D2 = map(int, input().split())

if D1 > D2:
    print(0)
elif D1 == D2:
    print(4)
elif D1 == D2 / 2:
    print(4)
elif D2 / 2 > D1:
    print(0)
else:
    print(8)
