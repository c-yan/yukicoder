from math import gcd
from functools import reduce

N, *A = map(int, open(0).read().split())

print(100 // reduce(gcd, A))
