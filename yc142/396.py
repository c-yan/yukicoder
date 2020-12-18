N, M = map(int, input().split())
X, Y = map(int, input().split())


def f(n):
    if (n - 1) // M % 2 == 0:
        return (n - 1) % M + 1
    else:
        return M - (n - 1) % M


if f(X) == f(Y):
    print('YES')
else:
    print('NO')
