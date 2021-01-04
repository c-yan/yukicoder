from heapq import heapify, heappop, heappush
from collections import Counter

N = int(input())
A = [input() for _ in range(N)]

c = Counter(A)
q = [(-c[k], k) for k in c]
heapify(q)

t = []
x, y = heappop(q)
t.append(y)
if x + 1 != 0:
    heappush(q, (x + 1, y))
while q:
    x, y = heappop(q)
    if t[-1] == y:
        if not q:
            print('NO')
            exit()
        m, n = heappop(q)
        t.append(n)
        if m + 1 != 0:
            heappush(q, (m + 1, n))
        heappush(q, (x, y))
    else:
        t.append(y)
        if x + 1 != 0:
            heappush(q, (x + 1, y))
print('YES')
