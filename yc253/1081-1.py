N = int(input())
A = list(map(int, input().split()))

m = 1000000007

fac = [0] * N
fac[0] = 1
for i in range(N - 1):
    fac[i + 1] = fac[i] * (i + 1) % m


def mcomb(n, k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0
    return fac[n] * pow(fac[n - k], m - 2, m) * pow(fac[k], m - 2, m) % m


result = 0
for i in range(N):
    result += mcomb(N - 1, i) * A[i]
    result %= m
print(result)
