S = input()

d = {}
for c in S:
    d.setdefault(c, 0)
    d[c] += 1

t = list(d.values())
if t.count(1) == 1 and t.count(2) == 6:
    print([k for k in d if d[k] == 1][0])
else:
    print('Impossible')
