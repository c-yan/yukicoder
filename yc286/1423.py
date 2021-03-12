from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    x = lcm(lcm(A, B), C)
    print(x + A, x + B, x + C)
