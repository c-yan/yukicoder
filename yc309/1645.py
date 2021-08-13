from collections import defaultdict

m = 998244353

N, *A = map(int, open(0).read().split())

d = {0: 1}
for a in A:
    t = defaultdict(int)
    for k in d:
        t[k + a] += d[k]
        t[k + a] %= m
        t[k - a] += d[k]
        t[k - a] %= m
    d = t

result = 0
for k in d:
    result += abs(k) * d[k]
    result %= m
print(result)
