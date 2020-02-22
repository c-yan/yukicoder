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

# Alice が橋を爆破する前のグループ数
groups = sum(1 for e in parent if e < 0)

# Alice が橋を1つ爆破した後のグループ数
if 1 in edges:
    groups += 1

# Bob が橋を1つ掛けた後のグループ数
if groups != 1:
    groups -= 1

if groups == 1:
    print('Bob')
else:
    print('Alice')
