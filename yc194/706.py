N = int(input())

d = {}
for _ in range(N):
    S = input()
    t = len(S) - 2
    d.setdefault(t, 0)
    d[t] += 1

t = max(d.values())
print(max(k for k in d if d[k] == t))
