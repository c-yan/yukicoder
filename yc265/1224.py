from math import gcd

a, b = map(int, input().split())

t = gcd(a, b)
b //= t
while b % 2 == 0:
    b //= 2
while b % 5 == 0:
    b //= 5

if b == 1:
    print('No')
else:
    print('Yes')
