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

parent = [-1] * N
d = {i: {} for i in range(N)}
vs = []
for _ in range(M):
    A, B = map(lambda x: int(x) - 1, readline().split())
    Y = int(readline())
    vs.append((A, B, Y))
    d[A][B] = Y
    d[B][A] = Y
    unite(parent, A, B)

result = [-1] * N
q = [i for i in range(N) if parent[i] < 0]
for i in q:
    result[i] = 0
while q:
    a = q.pop()
    for b in d[a]:
        if result[b] != -1:
            continue
        result[b] = result[a] ^ d[a][b]
        q.append(b)

for A, B, Y in vs:
    if result[A] ^ result[B] == Y:
        continue
    print(-1)
    exit()
print(*result, sep='\n')
