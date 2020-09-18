P, Q, R = map(int, input().split())

a = P / (P + Q + R)
b = Q / (P + Q + R)
c = R / (P + Q + R)

print(max(a, b, c, 1 - a, 1 - b, 1 - c))
