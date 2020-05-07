A, B, C = map(int, input().split())

print(min(abs(A - B), abs(A - C), abs(B - C)))
