from itertools import product

N = int(input())
A = list(map(int, input().split()))
B = [list(map(int, input().split())) for _ in range(N)]

W = -(10 ** 18)
for bits in product(range(2), repeat=N):
    if sum(bits) == 0:
        continue
    w = 0
    for i in range(N):
        if bits[i] == 1:
            w += A[i]
    for i in range(N):
        for j in range(i + 1, N):
            if bits[i] & bits[j] == 1:
                w += B[i][j]
    if w > W:
        W = w
        max_bits = bits
print(W)
print(*(i + 1 for i in range(N) if max_bits[i] == 1))
