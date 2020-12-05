P, Q = map(float, input().split())

p, q = P / 100, Q / 100

a = p * q
b = (1 - p) * (1 - q)
print(a / (a + b) * 100)
