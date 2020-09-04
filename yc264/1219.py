N, *A = map(int, open(0).read().split())

c = 0
for i in range(N - 1, -1, -1):
    if (A[i] + c) % (i + 1) != 0:
        print('No')
        break
    c += (A[i] + c) // (i + 1)
else:
    print('Yes')
