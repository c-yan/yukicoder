A, B, C, D = map(int, input().split())

B = min(A * C, B)
B = B // C * C
A = min(A, B // C)

print(min(D // (1 + C), A))
