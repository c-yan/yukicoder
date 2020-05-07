X, Y, Z = map(int, input().split())

result = Z
if X <= Z:
    result -= 1
if Y <= Z:
    result -= 1
print(result)
