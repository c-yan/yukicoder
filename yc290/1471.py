from sys import stdin

readline = stdin.readline

N, Q = map(int, readline().split())
S = readline()[:-1]

a = [0] * 26
b = []
for c in S:
    i = ord(c) - ord('a')
    a[i] += 1
    b.append(a[:])

result = []
for _ in range(Q):
    L, R, X = map(int, readline().split())
    t = b[R - 1][:]
    if L != 1:
        u = b[L - 2]
        for i in range(26):
            t[i] -= u[i]
    c = 0
    for i in range(26):
        c += t[i]
        if c < X:
            continue
        result.append(chr(i + ord('a')))
        break
print(*result, sep='\n')
