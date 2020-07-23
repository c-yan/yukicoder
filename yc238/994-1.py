# Union Find 木
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
    parent[j] += parent[i]
    parent[i] = j


setrecursionlimit(10 ** 6)


N, K = map(int, input().split())

parent = [-1] * N
for _ in range(N - 1):
    a, b = map(int, input().split())
    unite(parent, a - 1, b - 1)

if -parent[find(parent, 0)] >= K:
    print(K - 1)
else:
    print(-1)
