a, b, c, d, e, f = map(int, input().split())

y = (c - f * a / d) / (b - e * a / d)
x = c / a - (b / a) * y
print(x, y)
