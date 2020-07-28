from math import log2

A = int(input())
B = int(input())

t1 = (A / 5000) * 200000
t2 = (A / (5000 ** 2)) * (200000 ** 2)

if abs(1 - log2(B / t1)) < abs(1 - log2(B / t2)):
    print(1)
else:
    print(2)
