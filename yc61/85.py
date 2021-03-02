N, M, C = map(int, open(0).read().split())

if N > M:
    N, M = M, N

if N == 1 and M == 2:
    print('YES')
elif N == 1:
    print('NO')
elif N % 2 + M % 2 == 2:
    print('NO')
else:
    print('YES')
