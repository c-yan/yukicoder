m = 1000000007

N, K = map(int, input().split())

print((pow(N, K + 1, m) - N * pow(N - 1, K, m)) % m)
