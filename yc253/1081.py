N = int(input())
A = list(map(int, input().split()))

fac = [0] * N
fac[0] = 1
for i in range(N - 1):
    fac[i + 1] = fac[i] * (i + 1) % 1000000007


def mcomb(n, k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0
    return fac[n] * pow(fac[n - k], 1000000005, 1000000007) * pow(fac[k], 1000000005, 1000000007) % 1000000007


result = 0
for i in range(N):
    result += mcomb(N - 1, i) * A[i]
    result %= 1000000007
print(result)
