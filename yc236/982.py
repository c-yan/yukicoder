A, B = map(int, input().split())

if B < A:
    A, B = B, A

m = 120
max_x = (B * m + A - 1) // A
t = [0] * (A * max_x + B * m)
for x in range(max_x + 1):
    for y in range(m):
        t[A * x + B * y] = 1
c1 = t[:B * m].count(0)

m = 240
max_x = (B * m + A - 1) // A
t = [0] * (A * max_x + B * m)
for x in range(max_x + 1):
    for y in range(m):
        t[A * x + B * y] = 1
c2 = t[:B * m].count(0)

if c1 != c2:
    print(-1)
else:
    print(c1)
