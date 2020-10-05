from math import pi

C = int(input())
Rin, Rout = map(int, input().split())

x = (Rout - Rin) / 2
y = (Rout + Rin) / 2
print(C * 2 * x * x * y * pi * pi)
