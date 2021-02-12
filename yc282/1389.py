N, X, *S = map(int, open(0).read().split())

print(sum(S) - X * (N - 1))
