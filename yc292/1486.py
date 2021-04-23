from math import gcd

A, B, C, D, E = map(int, input().split())

x = (A + B) * (C + D) // gcd(A + B, C + D)
y = ([True] * A + [False] * B) * (x // (A + B))
z = ([True] * C + [False] * D) * (x // (C + D))

c = 0
for i in range(x):
    if not y[i] or not z[i]:
        continue
    c += 1

result = E // x * c
for i in range(E % x):
    if not y[i] or not z[i]:
        continue
    result += 1
print(result)
