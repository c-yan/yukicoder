from math import sqrt
from sys import stdin
from collections import deque

readline = stdin.readline

N, M = map(int, readline().split())
X, Y = map(lambda x: int(x) - 1, readline().split())
pq = [list(map(int, readline().split())) for _ in range(N)]
PQ = [list(map(int, readline().split())) for _ in range(M)]

links = [[] for _ in range(N)]
for P, Q in PQ:
    links[P - 1].append(Q - 1)
    links[Q - 1].append(P - 1)

q = deque([X])
t = [float('inf')] * N
t[X] = 0
while q:
    i = q.popleft()
    for j in links[i]:
        a, b = pq[i]
        c, d = pq[j]
        k = t[i] + sqrt((a - c) * (a -c) + (b - d) * (b - d))
        if k < t[j]:
            t[j] = k
            q.append(j)
print(t[Y])
