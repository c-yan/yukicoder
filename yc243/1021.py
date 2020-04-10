from collections import deque

N, M = map(int, input().split())
a = list(map(int, input().split()))
S = input()

q = deque(a)
for c in S:
    if c == 'L':
        t = q.popleft()
        q[0] += t
        q.append(0)
    elif c == 'R':
        t = q.pop()
        q[-1] += t
        q.appendleft(0)
print(*q)
