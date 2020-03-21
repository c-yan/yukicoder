A1, B1, A2, B2, A3, B3 = map(int, input().split())

t = A1 + A2 + A3
if t % 2 == 0:
    print(':-)')
else:
    print(':-(')
