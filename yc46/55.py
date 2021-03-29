from math import atan2, pi, sin, cos, sqrt

X1, Y1, X2, Y2, X3, Y3 = map(int, input().split())


def round(x):
    if x < 0:
        return int(x - 0.5)
    return int(x + 0.5)


def f(x1, y1, x2, y2, x3, y3):
    x, y = (x1 + x2) / 2, (y1 + y2) / 2
    r = sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1))
    t = atan2(y - y1, x - x1)
    x4 = round(x + r * cos(t + pi / 2))
    y4 = round(y + r * sin(t + pi / 2))
    x5 = round(x + r * cos(t - pi / 2))
    y5 = round(y + r * sin(t - pi / 2))
    if x3 == x4 and y3 == y4:
        return x5, y5
    elif x3 == x5 and y3 == y5:
        return x4, y4
    return None


result = f(X1, Y1, X2, Y2, X3, Y3)
if result is None:
    result = f(X1, Y1, X3, Y3, X2, Y2)
if result is None:
    result = f(X2, Y2, X3, Y3, X1, Y1)

if result is None:
    print(-1)
else:
    print(*result)
