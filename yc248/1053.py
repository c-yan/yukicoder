N = int(input())
A = list(map(int, input().split()))

d = {}
prev = -1
for a in A:
    if prev != a:
        d.setdefault(a, 0)
        d[a] += 1
    prev = a

if all(v == 1 for v in d.values()):
    print(0)
    exit()

if any(v >= 3 for v in d.values()):
    print(-1)
    exit()

if len([v for v in d.values() if v == 2]) == 1 and A[0] == A[-1]:
    print(1)
else:
    print(-1)
