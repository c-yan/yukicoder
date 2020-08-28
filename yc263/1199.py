from sys import stdin
readline = stdin.readline

N, M = map(int, readline().split())

odd, even = 0, 0
for _ in range(N):
    s = sum(map(int, readline().split()))
    t = odd
    odd = max(odd, even + s)
    even = max(even, t - s)
print(odd)
