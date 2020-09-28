N, *A = map(int, open(0).read().split())

t = {}
for a in A:
    t.setdefault(a, 0)
    t[a] += 1

print(list(t.values()).count(1))
