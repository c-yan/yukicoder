A, B, C = map(int, input().split())

A *= 60
C *= 3600
t = A - B
if t <= 0:
    print(-1)
else:
    print((C + t - 1) // t)
