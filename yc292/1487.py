from math import sqrt

def f(a, b, c):
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))

a, b, c = map(int, input().split())

print(f(a, b, c) / 4)
