N, K, X = map(int, input().split())

a = list(range(1, N + 1))
for _ in range(K):
    A, B = input().split()
    if A == '?':
        b = a[:]
        continue
    A, B = int(A) - 1, int(B) - 1
    a[A], a[B] = a[B], a[A]
C = list(map(int, input().split()))

c = [C[i] for i in range(N) if C[i] != a[i]]
print(*sorted([b.index(c[0]) + 1, b.index(c[1]) + 1]))
