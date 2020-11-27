N = int(input())

c = -1
t = N
while t != 0:
    c += 1
    t >>= 1

B = 1 << c
A = N ^ B
C = N

if A == 0:
    print(-1, -1, -1)
else:
    print(A, B, C)
