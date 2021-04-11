N, *A = map(int, open(0).read().split())

a, b, c = 0, 0, 0

for x in A:
    if x == 1:
        a += 1
    elif x == 2:
        b += 1
    elif x >= 3:
        c += 1

result = 0
result += a * (a - 1) // 2 * 2  # mex(1, 1)
result += a * b * 3             # mex(1, 2)
result += a * c * 2             # mex(1, >=3)
result += b * (b - 1) // 2 * 1  # mex(2, 2)
result += b * c * 1             # mex(2, >=3)
result += c * (c - 1) // 2 * 1  # mex(>=3, >=3)
print(result)
