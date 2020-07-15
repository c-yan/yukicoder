A0, B0, C0 = map(int, input().split('.'))
A1, B1, C1 = map(int, input().split('.'))

v0 = '%03d%03d%03d' % (A0, B0, C0)
v1 = '%03d%03d%03d' % (A1, B1, C1)

if v1 <= v0:
    print('YES')
else:
    print('NO')
