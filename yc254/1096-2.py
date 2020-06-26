N, *A = map(int, open(0).read().split())

result = 0
for i in range(N):
    # l = 0 .. i, r = i .. N - 1
    result += A[i] * (i + 1) * (N - i)
print(result)
