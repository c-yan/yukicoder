from sys import stdin

readline = stdin.readline

N, K = map(int, readline().split())
AB = [tuple(map(int, readline().split())) for _ in range(N)]


def is_ok(m):
    t = 0
    for A, B in AB:
        if m < A:
            continue
        if m >= B:
            t += B - A + 1
        else:
            t += m - A + 1
    return t >= K


ok = 10 ** 9 + 1
ng = 0
while ok - ng > 1:
    m = ng + (ok - ng) // 2
    if is_ok(m):
        ok = m
    else:
        ng = m
print(ok)
