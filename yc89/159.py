p, q = map(float, input().split())

P1 = (1 - p) * q
P2 = p * (1 - q) * q
if  P1 < P2:
    print('YES')
else:
    print('NO')
