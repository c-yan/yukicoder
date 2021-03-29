from sys import setrecursionlimit, stdin


def find(parent, i):
    t = parent[i]
    if t < 0:
        return i
    t = find(parent, t)
    parent[i] = t
    return t


def unite(parent, i, j):
    i = find(parent, i)
    j = find(parent, j)
    if i == j:
        return
    parent[j] += parent[i]
    parent[i] = j


readline = stdin.readline
setrecursionlimit(10 ** 6)

N, M = map(int, readline().split())

box = {}
color = {}
parent = [-1] * N
for i in range(N):
    b, c = map(int, readline().split())
    box.setdefault(b, [])
    box[b].append(i)
    color.setdefault(c, [])
    color[c].append(i)

for b in box.values():
    i = b[0]
    for j in b[1:]:
        unite(parent, i, j)

result = 0
for c in color.values():
    i = c[0]
    for j in c[1:]:
        if find(parent, i) == find(parent, j):
            continue
        result += 1
        unite(parent, i, j)
print(result)
