from functools import reduce


def f(x, y):
    t = x * y % 9
    if t == 0:
        return 9
    return t


N, *P = map(int, open(0).read().split())

if P.count(0) > 0:
    print(0)
else:
    print(reduce(f, P, 1))
