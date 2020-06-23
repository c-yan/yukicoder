from itertools import product

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)

c = 0
result = 0
for p in product([True, False], repeat=N - 1):
    t = K
    for i in range(N - 1):
        if p[i]:
            c += 1
            t %= A[i]
    c += 1
    t %= A[N - 1]
    result = max(result, t)
print(result)
print(c)
