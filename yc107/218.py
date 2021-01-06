a, b, c = map(int, open(0).read().split())

x = (a + b - 1) // b
y = (a + c - 1) // c

if 3 * y <= 2 * x:
    print('YES')
else:
    print('NO')
