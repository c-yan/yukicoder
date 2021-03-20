m = 1000000007

N = input()

t = [100, 50, 25, 20, 10, 5, 4, 2, 1]

mapping = {}
for x in t:
    mapping.setdefault(x, [-1] * 10)
    for y in range(1, 10):
        v = x * y
        for z in t:
            if v % z != 0:
                continue
            mapping[x][y] = z
            break

a, b = {1: 1}, {}
for c in N:
    na = {}
    nb = {1: 1}
    x = int(c)
    # a to a
    if x != 0:
        for k in a:
            z = mapping[k][x]
            na.setdefault(z, 0)
            na[z] += a[k]
            na[z] %= m
    # a to b
    for y in range(1, x):
        for k in a:
            z = mapping[k][y]
            nb.setdefault(z, 0)
            nb[z] += a[k]
            nb[z] %= m
    # b to b
    for y in range(1, 10):
        for k in b:
            z = mapping[k][y]
            nb.setdefault(z, 0)
            nb[z] += b[k]
            nb[z] %= m
    a, b = na, nb
a.setdefault(100, 0)
b.setdefault(100, 0)
print((a[100] + b[100]) % m)
