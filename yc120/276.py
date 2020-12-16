from math import gcd

N = int(input())

# gcd(N * (N + 1) // 2, N)
if N % 2 == 0:
    print(N // 2)
else:
    print(N)
