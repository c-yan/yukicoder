P, Q, R = map(int, input().split())
A, B, C = map(int, input().split())

nmin = max((A - 1) * P + 1, (A + B - 1) * Q + 1, (A + B + C - 1) * R + 1)
nmax = min(A * P, (A + B) * Q, (A + B + C) * R)

if nmin <= nmax:
    print(nmin, nmax)
else:
    print(-1)
