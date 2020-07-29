from sys import setrecursionlimit
from sys import stdin


def find(parent, amount, i):
    t = parent[i]
    if t < 0:
        return i, 0
    t, a = find(parent, amount, t)
    parent[i] = t
    amount[i] += a
    return t, amount[i]


def unite(parent, amount, i, j):
    i, _ = find(parent, amount, i)
    j, _ = find(parent, amount, j)
    if i == j:
        return
    parent[j] += parent[i]
    parent[i] = j
    amount[i] -= amount[j]


setrecursionlimit(10 ** 6)
readline = stdin.readline

N, Q = map(int, readline().split())

parent = [-1] * (N + 1)
amount = [0] * (N + 1)

result = []
for _ in range(Q):
    T, A, B = map(int, readline().split())
    if T == 1:
        unite(parent, amount, A, B)
    elif T == 2:
        j, _ = find(parent, amount, A)
        amount[j] += B
    elif T == 3:
        j, a = find(parent, amount, A)
        result.append(amount[j] + a)
print(*result, sep='\n')
