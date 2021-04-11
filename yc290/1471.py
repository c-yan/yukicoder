from sys import stdin

readline = stdin.readline

N, Q = map(int, readline().split())
S = readline()[:-1].encode('us-ascii')

a = [0] * 26
b = []
for c in S:
    i = c - 97
    a[i] += 1
    b.append(a[:])

result = []
for _ in range(Q):
    L, R, X = map(int, readline().split())
    L, R = L - 1, R - 1
    t = b[R][:]
    if L != 0:
        u = b[L - 1]
        for i in range(26):
            t[i] -= u[i]
    c = 0
    for i in range(26):
        c += t[i]
        if c < X:
            continue
        result.append(chr(i + 97))
        break
print(*result, sep='\n')
