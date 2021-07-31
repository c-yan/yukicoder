m = 1000000007

N, *c = map(int, open(0).read().split())

fac = [1] * (N + 1)
for i in range(N):
    fac[i + 1] = fac[i] * (i + 1)
    fac[i + 1] %= m

x = fac[N - 1] * (pow(10, N, m) - 1) * pow(9, -1, m) % m
frac = 0
denom = 1
for i in range(9):
    if c[i] == 0:
        continue
    frac += c[i] * (i + 1) * x
    frac %= m
    denom *= pow(fac[c[i]], -1, m)
    denom %= m
print(frac * denom % m)
