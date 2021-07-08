N, *A = map(int, open(0).read().split())

if sum(A) % N == 0:
    print('Yes')
else:
    print('No')
