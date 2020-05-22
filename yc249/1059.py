from sys import setrecursionlimit


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
    parent[i] += parent[j]
    parent[j] = i


setrecursionlimit(10 ** 6)

L, R = map(int, input().split())

parent = [-1] * (R + 1)
for i in range(L, R):
    if find(parent, i) != i:
        continue
    for j in range(i * 2, R + 1, i):
        unite(parent, i, j)
print(sum(1 for i in range(L, R + 1) if find(parent, i) == i) - 1)
