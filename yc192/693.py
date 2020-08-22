N, *A = map(int, open(0).read().split())

A.sort()
print(sum(abs(A[i] - (i + 1)) for i in range(N)))
