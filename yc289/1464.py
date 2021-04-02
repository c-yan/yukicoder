from decimal import Decimal
from math import gcd

X = Decimal(input())

r = 1
while X - int(X) != 0:
    X *= 10
    r *= 10

X =int(X)
n = gcd(X, r)
print('%d/%d' % (X // n, r // n))
