from functools import reduce
from math import gcd

n1 = int(input())
A = list(map(int, input().split()))
n2 = int(input())
B = list(map(int, input().split()))

a = A[0] * reduce(lambda x, y: x * y, B[1::2], 1)
b = reduce(lambda x, y: x * y, A[1:], 1) * reduce(lambda x, y: x * y, B[0::2], 1)
t = gcd(a, b)
a, b = a // t, b // t
if b < 0:
    a, b = -a, -b
print(a, b)
