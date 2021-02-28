from math import gcd


def lcm(x, y):
    return x // gcd(x, y) * y


N, D = map(int, input().split())

print(lcm(N, D) // D - 1)
