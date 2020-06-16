D1, D2, D3, S = map(int, input().split())

if S == 1 or sum([D1, D2, D3]) < 2:
    print('SURVIVED')
else:
    print('DEAD')
