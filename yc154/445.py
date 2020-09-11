def f(N, K):
    return 50 * N + 500 * N // (8 + 2 * K)


A, B = map(int, input().split())
print(f(A, B))
