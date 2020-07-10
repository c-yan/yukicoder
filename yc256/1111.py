N, M, K = map(int, input().split())

m = 1000000007

pqc = [[] * 301 for _ in range(301)]
for _ in range(M):
    P, Q, C = map(int, input().split())
    pqc[P].append((Q, C))

t = [{0: 1} for _ in range(301)]
for i in range(N - 1):
    nt = [{} for _ in range(301)]
    for j in range(1, 301):
        for k in t[j]:
            for q, c in pqc[j]:
                v = k + c
                if v <= K:
                    nt[q].setdefault(v, 0)
                    nt[q][v] += t[j][k]
                    nt[q][v] %= m
    t = nt

result = 0
for i in range(1, 301):
    t[i].setdefault(K, 0)
    result += t[i][K]
    result %= m
print(result)
