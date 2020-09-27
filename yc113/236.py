A, B, X, Y = map(int, input().split())

if Y * A > X * B:
    print(X + X * B / A)
else:
    print(Y + Y * A / B)
