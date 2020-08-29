from functools import cmp_to_key


def cmp(x, y):
    if x[0] != y[0]:
        return -(x[0] - y[0])
    else:
        return x[1] - y[1]


t = []
for c in 'ABC':
    H, W = map(int, input().split())
    t.append((H, W, c))
t.sort(key=cmp_to_key(cmp))
for _, _, result in t:
    print(result)
