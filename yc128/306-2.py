import numpy as np

xa, ya = map(int, input().split())
xb, yb = map(int, input().split())

def f(a, b, c):
    d = abs(b - c)
    return (a * a + d * d) ** 0.5

l = np.longdouble(0)
r = np.longdouble(1000)
for _ in range(100):
    a = f(xa, ya, (l * 2 + r) / 3) + f(xb, yb, (l * 2 + r) / 3)
    b = f(xa, ya, (l + r * 2) / 3) + f(xb, yb, (l + r * 2) / 3)
    if a < b:
        r = (l + r * 2) / 3
    else:
        l = (l * 2 + r) / 3
print((l + r) / 2)
