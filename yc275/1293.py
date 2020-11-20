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

N, D, W = map(int, readline().split())

car = [-1] * N
for _ in range(D):
    a, b = map(lambda x: int(x) - 1, readline().split())
    unite(car, a, b)

walking = [-1] * N
for _ in range(W):
    c, d = map(lambda x: int(x) - 1, readline().split())
    unite(walking, c, d)

xs = [i for i in range(N) if car[i] < 0]
cs = {}
ss = {}
for x in xs:
    cs[x] = 0
    ss[x] = set()

for i in range(N):
    a = find(car, i)
    b = find(walking, i)
    if b in ss[a]:
        continue
    ss[a].add(b)
    cs[a] -= walking[b]

result = 0
for x in xs:
    result -= car[x] * (cs[x] - 1)
print(result)
