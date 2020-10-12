from math import gcd

N, H, *A = map(int, open(0).read().split())

for a in A:
    t = gcd(a, H)
    H //= t
    if H == 1:
        break

if H == 1:
    print('YES')
else:
    print('NO')
