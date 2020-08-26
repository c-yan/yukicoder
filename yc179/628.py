N = int(input())

d = {}
for _ in range(N):
    No = int(input())
    M, S = map(int, input().split())
    Tag = input().split()
    for t in Tag:
        d.setdefault(t, 0)
        d[t] += S

for a, b in sorted((-d[k], k) for k in d)[:10]:
    print(b, -a)
