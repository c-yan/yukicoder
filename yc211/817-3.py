from sys import stdin
from itertools import accumulate

readline = stdin.readline

N, K = map(int, readline().split())
AB = [tuple(map(int, readline().split())) for _ in range(N)]

p = set()
for a, b in AB:
    p.add(a)
    p.add(b + 1)
inv = sorted(p)
fwd = {}
for i in range(len(inv)):
    fwd[inv[i]] = i

t = [0] * len(inv)
for a, b in AB:
    t[fwd[a]] += 1
    t[fwd[b + 1]] -= 1
t = list(accumulate(t))

c = 0
for i in range(len(t)):
    x = c + t[i] * (inv[i + 1] - inv[i])
    if x < K:
        c = x
        continue
    print(inv[i] + (K - c - 1) // t[i])
    break
