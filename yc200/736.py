from functools import reduce
from math import gcd

N, *a = map(int, open(0).read().split())

b = reduce(gcd, a)
print(*(i // b for i in a), sep=':')
