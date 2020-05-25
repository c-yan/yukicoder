N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

b = [0] * M
for a in A:
    for i in range(M):
        b[i] += a[i]

c = []
for a in A:
    t = 0
    for i in range(M):
        t += a[i] * b[i]
    c.append((t, a))
c.sort(reverse=True)

d = [0] * M
e = [0] * M
for i in range(N):
    if i % 2 == 0:
        t = d
    else:
        t = e
    _, a = c[i]
    for i in range(M):
        t[i] += a[i]
print(sum(t * t for t in d) - sum(t * t for t in e))
