N = int(input())

A = (2, 8)
B = (3, 9)
C = (7, 9)
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if A == (x1, y1):
        A = (x2, y2)
    if B == (x1, y1):
        B = (x2, y2)
    if C == (x1, y1):
        C = (x2, y2)

if A == (5, 8) and B == (4, 8) and C == (6, 8):
    print('YES')
else:
    print('NO')
