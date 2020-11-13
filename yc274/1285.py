from heapq import heappush, heapreplace

N, *A = map(int, open(0).read().split())

A.sort()
q = [A[0]]
for a in A[1:]:
    if a <= q[0] + 1:
        heappush(q, a)
    else:
        heapreplace(q, a)
print(len(q))
