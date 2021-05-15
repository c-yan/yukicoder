N, *A = map(int, open(0).read().split())

c = 0
l = 0
for i in range(N):
    if A[i] == 1:
        continue
    t = i - l + 1
    c += t * (t - 1) // 2
    l = i + 1
t = N - l + 1
c += t * (t - 1) // 2
print((N + 1) * N // 2 - c)
