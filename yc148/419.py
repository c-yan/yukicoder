a, b = map(int, input().split())

if a == b:
    print(abs(a * a + b * b) ** 0.5)
else:
    print(abs(a * a - b * b) ** 0.5)
