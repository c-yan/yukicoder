from sys import stdin

readline = stdin.readline

H, W, Q = map(int, readline().split())

c = H * W
t = {}
result = []
for _ in range(Q):
    Y, X = map(int, readline().split())
    t.setdefault(X - 1, H)
    p = t[X - 1]
    t[X - 1] = min(t[X - 1], Y - 1)
    c -= p - t[X - 1]
    result.append(c)
print(*result, sep='\n')
