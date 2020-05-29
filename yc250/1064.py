a, b, c, d = map(int, input().split())


def f(x):
    return 2 * x * x + (a - c) * x + (b - d)


t = f((c - a) / 4)

if abs(t) < 1e-6:
    print('Yes')
    exit()

if t > 0:
    print('No')
    exit()

ok = (c - a) / 4
ng = 1e12
for _ in range(100):
    m = (ok + ng) / 2
    if f(m) < 0:
        ok = m
    else:
        ng = m
x1 = ng
y1 = x1 * x1 + a * x1 + b

ok = (c - a) / 4
ng = -1e12
for _ in range(100):
    m = (ok + ng) / 2
    if f(m) < 0:
        ok = m
    else:
        ng = m
x2 = ng
y2 = x2 * x2 + a * x2 + b

p = (y2 - y1) / (x2 - x1)
q = y1 - p * x1
print(p, q)
