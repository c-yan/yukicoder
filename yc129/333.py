A, B = map(int, input().split())

if A > B:
    print(2000000000 - B - 1)
else:
    print(B - 1 - 1)
