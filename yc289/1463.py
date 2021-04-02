from itertools import product
from functools import reduce

N, K, *A = map(int, open(0).read().split())

s = set()
for p in product([True, False], repeat=N):
    if list(p).count(True) < K:
        continue
    s.add(sum(A[i] for i in range(N) if p[i]))
    s.add(reduce(lambda x, y: x * y, (A[i] for i in range(N) if p[i])))
print(len(s))
