from sys import stdin
from heapq import heapify, heappop, heappush

readline = stdin.readline

N = int(readline())
S = list(readline()[:-1])
T = list(readline()[:-1])
Q = int(readline())

s = set()
q = []
for i in range(N):
    if S[i] == T[i]:
        continue
    q.append(i)
    s.add(i)
heapify(q)

result = []
for _ in range(Q):
    c, x, y = readline().split()
    x = int(x) - 1

    is_same = S[x] == T[x]
    if c == 'S':
        S[x] = y
    elif c == 'T':
        T[x] = y
    if (S[x] == T[x]) != is_same:
        if is_same:
            heappush(q, x)
            s.add(x)
        else:
            s.remove(x)

    while len(q) != 0 and q[0] not in s:
        heappop(q)

    if len(q) == 0:
        result.append('=')
        continue

    p = q[0]
    if S[p] > T[p]:
        result.append('>')
    elif S[p] < T[p]:
        result.append('<')
print(*result, sep='\n')
