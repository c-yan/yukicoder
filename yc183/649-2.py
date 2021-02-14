from sys import stdin
from heapq import heappop, heappush

readline = stdin.readline

Q, K = map(int, readline().split())

result = []
q0 = []
q1 = []
for _ in range(Q):
    query = readline()
    if query[0] == '1':
        v = int(query[2:])
        if len(q0) < K:
            heappush(q0, -v)
        else:
            if -q0[0] > v:
                heappush(q1, -heappop(q0))
                heappush(q0, -v)
            else:
                heappush(q1, v)
    elif query[0] == '2':
        if len(q0) < K:
            result.append(-1)
        else:
            result.append(-heappop(q0))
            if len(q1) > 0:
                heappush(q0, -heappop(q1))
print(*result, sep='\n')
