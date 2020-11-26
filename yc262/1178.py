a, b, c, d, e, f = map(int, input().split())

x = c / a / 2
y = d / a / 2
t = f / a - e / a + x * x + y * y
print(t ** 0.5)
