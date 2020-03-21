X, Y, Z = map(int, input().split())

if X > Y:
    X, Y = Y, X

if Y - X > Z:
    print(X + Z)
else:
    print(Y + (Z - (Y - X)) // 2)
