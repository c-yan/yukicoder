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


result = 0
for i in range(1, M + 1):
    result = mcomb(M, i) * pow(i, N, m) - result
    result %= m

print(result)
