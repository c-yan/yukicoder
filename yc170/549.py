N, *x = map(int, open(0).read().split())

print((max(x) + 1) // 2 + sum(a // 2 for a in x))
