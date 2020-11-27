N, K, *A = map(int, open(0).read().split())

m = 998244353

print(sum(A) * pow(2, K, m) % m)
