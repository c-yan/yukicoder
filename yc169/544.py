N = int(input())

A = 0
B = 0
M = 1
while N != 0:
    if N % 10 == 7:
        A += 6 * M
        B += 1 * M
    else:
        A += (N % 10) * M
    N //= 10
    M *= 10
print(A, B)
