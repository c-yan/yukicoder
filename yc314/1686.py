N, *P = map(int, open(0).read().split())

t = set(P)
print(sum(x for x in P if x - 1 not in t))
