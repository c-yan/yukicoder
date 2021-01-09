from heapq import heappop, heappush

N, M, P, *A = map(int, open(0).read().split())


def f(x):
    c = 0
    while x % P == 0:
        c += 1
        x //= P
    return (x, c)


max_A = max(A)

if max_A > M:
    print(1)
    exit()

b = {}
for m, c in map(f, A):
    b.setdefault(c, 0)
    b[c] = max(b[c], m)
t = 1
for k in sorted(b):
    if b[k] <= t:
        del b[k]
    else:
        t = b[k]

if len(b) == 0:
    print(-1)
    exit()

q = [(0, 1)]
max_x = {}
max_x[0] = 1
while q:
    c, x = heappop(q)
    if max_x[c] > x:
        continue
    if x * max_A > M:
        print(c + 1)
        break
    for k in b:
        nc = c + 1 + k
        nx = x * b[k]
        max_x.setdefault(nc, 0)
        if nx > max_x[nc]:
            max_x[nc] = nx
            heappush(q, (nc, nx))
