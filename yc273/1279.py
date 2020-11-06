from itertools import permutations

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = {}
for x in permutations(a):
    t = 0
    for i in range(N):
        t += max(x[i] - b[i], 0)
    d.setdefault(t, 0)
    d[t] += 1
print(d[max(d)])
