S = input()

d = {}
for c in S:
    d.setdefault(c, 0)
    d[c] += 1

if all(map(lambda x: x == 1, d.values())):
    print('YES')
else:
    print('NO')
