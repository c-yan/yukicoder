from sys import stdin
from itertools import accumulate

readline = stdin.readline


def shrink(a):
    inv = sorted(set(a))
    n = len(inv)
    fwd = {}
    for i in range(n):
        fwd[inv[i]] = i
    return n, fwd, inv


N, K = map(int, readline().split())
AB = [tuple(map(int, readline().split())) for _ in range(N)]

p = []
for a, b in AB:
    p.append(a)
    p.append(b + 1)
n, fwd, inv = shrink(p)

t = [0] * n
for a, b in AB:
    t[fwd[a]] += 1
    t[fwd[b + 1]] -= 1
t = list(accumulate(t))

c = 0
for i in range(n):
    x = c + t[i] * (inv[i + 1] - inv[i])
    if x < K:
        c = x
        continue
    print(inv[i] + (K - c - 1) // t[i])
    break
