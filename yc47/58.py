N = int(input())
K = int(input())

dp1 = {0: 1}
for _ in range(K):
    d = {}
    for k in dp1:
        for i in range(4, 6 + 1):
            d.setdefault(k + i, 0)
            d[k + i] += dp1[k] * 2
    dp1 = d
for _ in range(N - K):
    d = {}
    for k in dp1:
        for i in range(1, 6 + 1):
            d.setdefault(k + i, 0)
            d[k + i] += dp1[k]
    dp1 = d

dp2 = {0: 1}
for _ in range(N):
    d = {}
    for k in dp2:
        for i in range(1, 6 + 1):
            d.setdefault(k + i, 0)
            d[k + i] += dp2[k]
    dp2 = d

t = 0
for a in dp1:
    for b in dp2:
        if a <= b:
            continue
        t += dp1[a] * dp2[b]
result = t / pow(6, N * 2)
print(result)
