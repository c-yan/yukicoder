from math import log2


def is_ok(N):
    return N * N <= Q * log2(N) * N + P


P, Q = map(int, input().split())

ok = 1
ng = 1e12
for _ in range(100):
    m = (ok + ng) / 2
    if is_ok(m):
        ok = m
    else:
        ng = m

print(ok)
