A, B = map(int, input().split())

if min(A, B) % 2 == 1 and abs(A - B) <= 1:
    print('Q')
else:
    print('P')
