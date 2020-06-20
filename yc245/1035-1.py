from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

N, M = map(int, input().split())

m = 1000000007

fac = [0] * (M + 1)
fac[0] = 1
for i in range(M):
    fac[i + 1] = fac[i] * (i + 1) % m


def mcomb(n, k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0
    return fac[n] * pow(fac[n - k], m - 2, m) * pow(fac[k], m - 2, m) % m


def f(i):
    if i == 0:
        return 0
    return (mcomb(M, i) * pow(i, N, m) - f(i - 1)) % m


print(f(M))
