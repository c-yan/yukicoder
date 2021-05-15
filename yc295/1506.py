from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

N, *A = map(int, open(0).read().split())

cache = [[None] * (N + 1) for _ in range(2)]


def f(i, turn):
    if i == 0:
        return turn ^ 1

    if cache[turn][i] is not None:
        return cache[turn][i]

    if A[i - 1] == 1:
        t = f(i - 1, turn ^ 1)
        cache[turn][i] = t
        return t

    t = f(i - 1, turn)
    if t == turn:
        cache[turn][i] = t
        return t
    t = f(i - 1, turn ^ 1)
    cache[turn][i] = t
    return t


if f(N, 0) == 0:
    print('Alice')
else:
    print('Bob')
