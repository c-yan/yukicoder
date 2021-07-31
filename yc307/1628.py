N, *c = map(int, open(0).read().split())

t = []
for i in range(9):
    for _ in range(c[i]):
        t.append(i + 1)

print(''.join(str(i) for i in sorted(t, reverse=True)))
