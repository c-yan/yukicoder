N, *A = map(int, open(0).read().split())

c = 0
i = 0
while i < N - 1:
    if A[i] > A[i + 1]:
        c += 1
        i += 1
    i += 1
print(N - c)
