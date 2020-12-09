from collections import deque

N = int(input())

INF = 10 ** 12

t = [INF] * N
t[0] = 0

q = deque([0])
while q:
    a = q.popleft()
    d = bin(a + 1).count(1)
    if a - d > 0 and t[a - d] > t[a] + 1:
        t[a - d] = t[a] + 1
        q.append(a - d)
    if a + d < N and t[a + d] > t[a] + 1:
        t[a + d] = t[a] + 1
        q.append(a + d)

if t[N - 1] == INF:
    print(-1)
else:
    print(t[N - 1])
