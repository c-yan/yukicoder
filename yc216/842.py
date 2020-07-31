A, B, C, D, E, F, G = map(int, input().split())

t = G // 500
G -= 500 * min(t, A)

t = G // 100
G -= 100 * min(t, B)

t = G // 50
G -= 50 * min(t, C)

t = G // 10
G -= 10 * min(t, D)

t = G // 5
G -= 5 * min(t, E)

t = G // 1
G -= 1 * min(t, F)

if G == 0:
    print('YES')
else:
    print('NO')
