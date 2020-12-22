b1, b2, b3 = map(int, input().split())

r = (b3 - b2) / (b2 - b1)
d = b3 - r * b2
b4 = r * b3 + d
if b4 <= -0.5:
    b4 -= 0.5
else:
    b4 += 0.5
print(int(b4))
