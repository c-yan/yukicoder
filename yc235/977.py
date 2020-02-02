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


setrecursionlimit(10 ** 5)

N = int(input())

parent = [-1] * N
edges = [0] * N
for _ in range(N - 1):
    u, v = map(int, input().split())
    unite(parent, u, v)
    edges[u] += 1
    edges[v] += 1

t = sum(1 for e in parent if e < 0)
if 1 in edges:
    t += 1

if t >= 3:
    print('Alice')
else:
    print('Bob')
