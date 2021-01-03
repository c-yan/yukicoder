N, M, *A = map(int, open(0).read().split())

t = list(range(1, N + 1))
for a in A:
    x = t[a - 1]
    t[1:a] = t[:a - 1]
    t[0] = x
print(t[0])
