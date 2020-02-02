K, N, F = map(int, input().split())
A = list(map(int, input().split()))

t = K * N - sum(A)
if t < 0:
    print(-1)
else:
    print(t)
