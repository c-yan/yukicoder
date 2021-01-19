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
    parent[i] += parent[j]
    parent[j] = i


readline = stdin.readline
setrecursionlimit(10 ** 6)

N, M = map(int, readline().split())

parent = [-1] * N
for _ in range(M):
    A, B = map(lambda x: int(x) - 1, readline().split())
    i = find(parent, A)
    j = find(parent, B)
    if -parent[i] > -parent[j]:
        unite(parent, i, j)
    elif -parent[i] < -parent[j]:
        unite(parent, j, i)
    elif -parent[i] == -parent[j]:
        if i < j:
            unite(parent, i, j)
        else:
            unite(parent, j, i)

result = [0] * N
for i in range(N):
    result[i] = find(parent, i) + 1
print(*result, sep='\n')
