X, Y, L = map(int, open(0).read().split())

result = 0
if Y > 0:
    result += (Y + (L - 1)) // L

if X != 0:
    result += 1
    result += (abs(X) + (L - 1)) // L

if Y < 0:
    if X == 0:
        result += 1
    result += 1
    result += (-Y + (L - 1)) // L

print(result)
