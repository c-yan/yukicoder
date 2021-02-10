N, M, K = map(int, input().split())
abc = [tuple(map(int, input().split())) for _ in range(M)]
d = list(map(int, input().split()))

links = {}
for a, b, c in abc:
    links.setdefault(c, [])
    links[c].append((a - 1, b - 1))

q = set(range(N))
for k in range(K):
    nq = set()
    l = links[d[k]]
    for i in q:
        for a, b in l:
            if i == a:
                nq.add(b)
            if i == b:
                nq.add(a)
    q = nq
print(len(q))
print(*sorted(i + 1 for i in q))
