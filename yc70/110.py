from bisect import bisect_left

Nw = int(input())
W = list(map(int, input().split()))
Nb = int(input())
B = list(map(int, input().split()))

W.sort()
B.sort()

a = 0
t = 0
while True:
    i = bisect_left(W, t + 1)
    if i == Nw:
        break
    t = W[i]
    a += 1
    i = bisect_left(B, t + 1)
    if i == Nb:
        break
    t = B[i]
    a += 1

b = 0
t = 0
while True:
    i = bisect_left(B, t + 1)
    if i == Nb:
        break
    t = B[i]
    b += 1
    i = bisect_left(W, t + 1)
    if i == Nw:
        break
    t = W[i]
    b += 1

print(max(a, b))
