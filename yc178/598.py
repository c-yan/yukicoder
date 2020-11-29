N, X, A, B = map(int, open(0).read().split())

print(min((X + A - 1) // A, ((1 << (N - 1)) - X + B - 1) // B))
