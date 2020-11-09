A, B = map(int, input().split())


def is_ok(A, B, C):
    return A != C and B != C and (A + B) % C == 0 and (A + C) % B == 0 and (B + C) % A == 0


result = -1
for i in range(1, int((A + B) ** 0.5) + 1):
    for C in [i, (A + B) // i]:
        if is_ok(A, B, C):
            if result == -1:
                result = C
            else:
                result = min(result, C)
print(result)
