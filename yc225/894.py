from fractions import gcd


def lcm(x, y):
    return (x * y) // gcd(x, y)


T, A, B = map(int, input().split())

print(((T - 1) // A + 1) + ((T - 1) // B + 1) - ((T - 1) // lcm(A, B) + 1))
