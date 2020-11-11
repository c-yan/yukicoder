from collections import deque

N = int(input())

t = set([N])
q = deque([N])
while q:
    i = q.popleft()
    for a in [i // 3, i // 5]:
        if a in t:
            continue
        t.add(a)
        q.append(a)

d = {}
d[0] = 1
t.remove(0)
for i in sorted(t):
    d[i] = d[i // 3] + d[i // 5]
print(d[N])
