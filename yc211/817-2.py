from sys import stdin

readline = stdin.readline

N, K = map(int, readline().split())

d = {}
for _ in range(N):
    A, B = map(int, readline().split())
    d.setdefault(A, 0)
    d[A] += 1
    d.setdefault(B + 1, 0)
    d[B + 1] -= 1

skeys = sorted(d)
for i in range(len(skeys) - 1):
    d[skeys[i + 1]] += d[skeys[i]]

c = 0
for i in range(len(skeys) - 1):
    x = c + d[skeys[i]] * (skeys[i + 1] - skeys[i])
    if x < K:
        c = x
        continue
    print(skeys[i] + (K - c - 1) // d[skeys[i]])
    break
