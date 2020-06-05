N, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

d = {}
for a in A:
    d.setdefault(a, 0)
    d[a] += 1

result = 0
if X == 0:
    for v in d.values():
        result += v * (v - 1) // 2
    print(result)
else:
    for k in d:
        if k ^ X in d:
            result += d[k] * d[k ^ X]
    print(result // 2)
