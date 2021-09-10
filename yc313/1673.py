from sys import stdin

readline = stdin.readline

N, Q = map(int, readline().split())

c = 0
t = [0] * (N + 1)
result = []
for _ in range(Q):
    L, R = map(int, readline().split())
    for i in range(L - 1, R):
        if t[i] == 0:
            c += 1
            t[i] = 1
        elif t[i] == 1:
            c -= 1
            t[i] = 0
    result.append(c)
print(*result, sep='\n')
