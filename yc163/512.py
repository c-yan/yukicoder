X, Y, N, *A = map(int, open(0).read().split())

for i in range(1, N):
    if X * A[i] >= A[i - 1] * Y:
        continue
    print('NO')
    break
else:
    print('YES')
