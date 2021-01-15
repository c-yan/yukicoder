from sys import setrecursionlimit, stdin


def find(parent, i):
    t = parent[i]
    if t < 0:
        return i
    t = find(parent, t)
    parent[i] = t
    return t


def unite(parent, i, j):
    i = find(parent, i)
    j = find(parent, j)
    if i == j:
        return
    parent[j] += parent[i]
    parent[i] = j


def make_prime_table(n):
    sieve = list(range(n + 1))
    sieve[0] = -1
    sieve[1] = -1
    for i in range(4, n + 1, 2):
        sieve[i] = 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i] != i:
            continue
        for j in range(i * i, n + 1, i * 2):
            if sieve[j] == j:
                sieve[j] = i
    return sieve


readline = stdin.readline
setrecursionlimit(10 ** 6)

N, P = map(int, readline().split())

parent = [-1] * (N + 1)
sieve = make_prime_table(N)
for j in range(2 * 2, N + 1, 2):
    unite(parent, 2, j)
for i in range(3, N + 1, 2):
    if sieve[i] != i:
        continue
    if 2 * i <= N:
        unite(parent, 2, i)
    for j in range(i * i, N + 1, i * 2):
        unite(parent, i, j)
print(-parent[find(parent, P)])
