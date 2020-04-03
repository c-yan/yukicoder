from heapq import heapify, heappop, heappush

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))

A = [-a for a in A]
heapify(A)

while A:
    if Z == 0:
        break
    x = -heappop(A)
    if x >= 10000:
        t = min(x // 10000, Z)
        Z -= t
        x -= 10000 * t
        heappush(A, -x)
    else:
        Z -= 1

while A:
    if Y == 0:
        break
    x = -heappop(A)
    if x >= 5000:
        t = min(x // 5000, Y)
        Y -= t
        x -= 5000 * t
        heappush(A, -x)
    else:
        Y -= 1

while A:
    if X == 0:
        break
    x = -heappop(A)
    t = min((x + 1000) // 1000, X)
    X -= t
    x -= t * 1000
    if x >= 0:
        heappush(A, -x)

if len(A) == 0:
    print('Yes')
else:
    print('No')
