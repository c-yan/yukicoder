from math import gcd, isqrt

A, B = map(int, input().split())

X = gcd(A, B)

if isqrt(X) * isqrt(X) == X:
    print('Odd')
else:
    print('Even')
