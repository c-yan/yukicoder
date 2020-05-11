from math import gcd

A, B = map(int, input().split())

if gcd(A, B) != 1:
    print(-1)
    exit()

n = A * B
t = [0] * (n + 1)
for x in range(B + 1):
    for y in range(A + 1):
        z = A * x + B * y
        if z > n:
            continue
        t[z] = 1
print(t.count(0))
