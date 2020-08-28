from sys import stdin
readline = stdin.readline

N, M = map(int, readline().split())

a, b = 0, 0
for _ in range(N):
    t = sum(map(int, readline().split()))
    c, d = a, b
    a = max(c, d + t)
    b = max(d, c - t)
print(max(a, b))
