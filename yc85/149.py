Aw, Ab = map(int, input().split())
Bw, Bb = map(int, input().split())
C, D = map(int, input().split())

b = min(C, Ab)
w = C - b

Aw -= w
Ab -= b
Bw += w
Bb += b

w = min(D, Bw)
b = D - w

Aw += w
Ab += b
Bw -= w
Bb -= b

print(Aw)
