from sys import stdin

readline = stdin.readline

N, M = map(int, readline().split())
LR = [list(map(int, readline().split())) for _ in range(M)]

result = N
t = -1
for L, R in sorted(LR, key=lambda x: x[1]):
    if L <= t <= R:
        continue
    result -= 1
    t = R
print(result)
